from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  View)
from django.contrib.auth.mixins import LoginRequiredMixin
from .. import models
from .. import forms
from ...handbooks import models as hmodels
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.conf import settings
from dbfread import DBF
from itertools import zip_longest
from apps.handbooks import forms as h_forms
from apps.handbooks import models as h_models
from django.shortcuts import render
from django.views.generic.edit import BaseFormView
import tempfile
from django.db.models import OuterRef, Subquery
from django.db.models import Prefetch


class PassportListView(LoginRequiredMixin, ListView):
    """
        Passport List View
    """
    template_name = 'passport/moc_list.html'
    model = models.MocList
    paginate_by = settings.DEFAULT_PAGE_SIZE
    ordering = 'id'

    def get_paginate_by(self, queryset):
        if 'no_page' in self.request.GET:
            return None
        user_settings = self.request.user.usersettings
        pagination_size = user_settings.pagination_size
        return pagination_size if pagination_size else self.paginate_by

    def get_queryset(self):
        latest_device_location_query = models.DeviceLocation.objects.filter(
                    moc_list=OuterRef('pk')
                ).order_by('-entry_date')
        queryset = models.MocList.objects.prefetch_related(
            'device_location',
            'verification_info',
            'repair_info',
            'device_status_date',
            'moc_metals').annotate(
                last_device_location_workshop=Subquery(
                    latest_device_location_query.values(
                        'department__workshop')[:1]),
                last_device_location_brigade=Subquery(
                    latest_device_location_query.values(
                        'department__brigade')[:1]),
                ).values(
                    'id',
                    'moc_group__id',
                    'moc_group__name',
                    'moc_type__id',
                    'moc_type__type',
                    'factory_number',
                    'inv_number',
                    'last_device_location_workshop',
                    'last_device_location_brigade',
                    ).all().order_by('-id')
        query = self.request.GET.get('q')

        if query:
            # Filter the queryset
            queryset = queryset.filter(
                Q(moc_group__name__icontains=query) |
                Q(moc_type__type__icontains=query) |
                Q(inv_number__icontains=query)
            ).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # paginaton, deal wih too many pages
        page = context['page_obj']
        if page:
            context['paginator_range'] = page.paginator.get_elided_page_range(
                page.number, on_each_side=2, on_ends=1
            )
        form = forms.MocListForm()
        migration_form = forms.FileUploadForm()
        migration_form.fields['select_model'].choices = [
            ('moc_list', 'Паспорта'),
            ('moc_metals', 'Металлы'),
            ('verification_info', 'Поверки'),
            ('repair_info', 'Ремонты'),
            ('device_location', 'Места закрепления'),
            ('device_status', 'Статусы'),
            ('device_station', 'Оборудование')]

        context['form'] = form
        context['migration_form'] = migration_form
        return context


class MocListDetailView(LoginRequiredMixin, DetailView):
    """
        DetailView for MocList
    """
    template_name = 'passport/passport_main.html'
    model = models.MocList
    form_class = forms.MocListForm
    success_url = reverse_lazy('passport')

    def get_queryset(self):
        return models.MocList.objects.prefetch_related(
            # Сортировка по убыванию (сначала новые)
            Prefetch(
                'device_location',
                queryset=models.DeviceLocation.objects.order_by(
                    '-entry_date')),
            Prefetch(
                'verification_info',
                queryset=models.VerificationInfo.objects.order_by(
                    '-entry_date')),
            Prefetch(
                'repair_info',
                queryset=models.RepairInfo.objects.order_by(
                    '-entry_date')),
            Prefetch(
                'device_status_date',
                queryset=models.DeviceStatusDate.objects.order_by(
                    '-status_date')),
            Prefetch(
                'moc_metals',
                queryset=models.MocMetals.objects.order_by(
                    '-id'))
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.MocListForm
        context['table_forms'] = {'verification': forms.VerificationInfoForm,
                                  'repair': forms.RepairInfoForm,
                                  'location': forms.DeviceLocationForm,
                                  'status': forms.DeviceStatusDateForm,
                                  'metall': forms.MocMetalsForm}
        return context


class PassportPrintView(LoginRequiredMixin, DetailView):
    """
        DetailView for printing Passport
    """
    template_name = 'passport/passport_print.html'
    model = models.MocList
    form_class = forms.MocListForm
    success_url = reverse_lazy('passport')

    def get_queryset(self):
        queryset = models.MocList.objects.prefetch_related(
            'device_location',
            'verification_info',
            'repair_info',
            'device_status_date',
            'moc_metals').all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verification_list = self.get_object().verification_info.all()
        repair_list = self.get_object().repair_info.all()
        data_list = zip_longest(verification_list, repair_list)
        context['data_list'] = data_list
        return context


class MocListCreateView(LoginRequiredMixin, CreateView):
    """
        CreateView for MocList
    """
    model = models.MocList
    form_class = forms.MocListForm
    success_url = reverse_lazy('passport')


class MocListUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for MocList
    """
    model = models.MocList
    form_class = forms.MocListForm
    success_url = reverse_lazy('passport')

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        back_url = request.META.get('HTTP_REFERER', '/')
        response = HttpResponseRedirect(back_url)
        return response


class MocListDeleteView(LoginRequiredMixin, DeleteView):
    """
        DeleteView for MocList
    """
    model = models.MocList
    form_class = forms.MocListForm
    success_url = reverse_lazy('passport')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = HttpResponseRedirect(self.get_success_url())
        response.status_code = 303
        return response


class PassportMocTypeView(LoginRequiredMixin, BaseFormView):
    """
        Get modal for adding new MocType
    """
    model = h_models.MocType
    form_class = h_forms.MocTypeForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
        new_form = forms.MocListForm()
        return render(request,
                      'passport/modals/moc_list_modal.html',
                      {'form': new_form})

    def get(self, request, *args, **kwargs):
        form = h_forms.MocTypeForm()
        return render(request,
                      'handbooks/modals/passport_moc_type_modal.html',
                      {'form': form})


class PassportChangeTypeView(LoginRequiredMixin, BaseFormView):
    """
        Get modal for adding new ChangeType
    """
    model = h_models.ChangeType
    form_class = h_forms.ChangeTypeForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
        new_form = forms.MocListForm()
        return render(request,
                      'passport/modals/moc_list_modal.html',
                      {'form': new_form})

    def get(self, request, *args, **kwargs):
        form = h_forms.ChangeTypeForm()
        return render(request,
                      'handbooks/modals/passport_change_type_modal.html',
                      {'form': form})


class PassportMocGroupView(LoginRequiredMixin, BaseFormView):
    """
        Get modal for adding new MocGroup
    """
    model = h_models.MocGroup
    form_class = h_forms.MocGroupForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
        new_form = forms.MocListForm()
        return render(request,
                      'passport/modals/moc_list_modal.html',
                      {'form': new_form})

    def get(self, request, *args, **kwargs):
        form = h_forms.MocGroupForm()
        return render(request,
                      'handbooks/modals/passport_moc_group_modal.html',
                      {'form': form})


class PassportVerificationDepartmentView(LoginRequiredMixin, BaseFormView):
    """
        Get modal for adding new VerificationDepartment
    """
    model = h_models.VerificationDepartment
    form_class = h_forms.VerificationDepartmentForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
        new_form = forms.MocListForm()
        return render(request,
                      'passport/modals/moc_list_modal.html',
                      {'form': new_form})

    def get(self, request, *args, **kwargs):
        form = h_forms.VerificationDepartmentForm()
        return render(request,
                      'handbooks/modals/passport_verification_department_modal.html',
                      {'form': form})


class PassportMigrateView(LoginRequiredMixin, View):
    success_url = reverse_lazy('passport')

    def post(self, request, *args, **kwargs):
        form = forms.FileUploadForm(request.POST, request.FILES)
        form.fields['select_model'].choices = [
            ('moc_list', 'Паспорта'),
            ('moc_metals', 'Металлы'),
            ('verification_info', 'Поверки'),
            ('repair_info', 'Ремонты'),
            ('device_location', 'Места закрепления'),
            ('device_status', 'Статусы'),
            ('device_station', 'Оборудование')]
        if form.is_valid():
            uploaded_file = request.FILES['file']
            with tempfile.NamedTemporaryFile(suffix='.dbf', delete=True) as temp_file:
                for chunk in uploaded_file.chunks():
                    temp_file.write(chunk)
                temp_file.flush()

                match form.cleaned_data['select_model']:
                    case 'moc_list':
                        models.MocList.objects.all().delete()
                        self.copy_moc_list(temp_file.name)
                    case 'moc_metals':
                        models.MocMetals.objects.all().delete()
                        self.copy_moc_metals(temp_file.name)
                    case 'verification_info':
                        models.VerificationInfo.objects.all().delete()
                        self.copy_verification_info(temp_file.name)
                    case 'repair_info':
                        models.RepairInfo.objects.all().delete()
                        self.copy_repair_info(temp_file.name)
                    case 'device_location':
                        models.DeviceLocation.objects.all().delete()
                        self.copy_device_location(temp_file.name)
                    case 'device_status':
                        models.DeviceStatusDate.objects.all().delete()
                        self.copy_device_status(temp_file.name)
                    case 'device_station':
                        models.DeviceStation.objects.all().delete()
                        self.copy_device_station(temp_file.name)

        return HttpResponseRedirect(self.success_url)

    def copy_moc_list(self, uploaded_file):
        # dbf/maa/maa01.DBF
        table = DBF(uploaded_file)

        data_list = []
        for record in table:
            new_dict = {}
            try:
                new_dict['moc_type'] = hmodels.MocType.objects.filter(
                    type=record.get('TIP_SI')
                    ).first()
                new_dict['factory_number'] = record.get('ZAV_N')
                new_dict['inv_number'] = record.get('INV_N')
                new_dict['change_type'] = hmodels.ChangeType.objects.get(
                    code=record.get('VID_IZ')
                    )
                new_dict['moc_group'] = hmodels.MocGroup.objects.filter(
                        group=record.get('GR_SI'),
                        type=record.get('VID_IZ')).first()
                new_dict['verification_type'] = record.get('VID_POV')
                new_dict['sign_o_r'] = record.get('PR_O_R')
                new_dict['sign_o_m'] = record.get('PR_O_M')
                new_dict['verification_period'] = record.get('PER_POV')
                new_dict['verification_department'] = hmodels.VerificationDepartment.objects.filter(
                    code=record.get('POV_POD')
                    ).first()
                data_list.append(new_dict)
            except Exception as e:
                error_type = type(e).__name__
                print(f"{error_type}: {e}")
                print(record)

        obj_list = [models.MocList(**data_dict) for data_dict in data_list]
        models.MocList.objects.bulk_create(obj_list)

    def copy_moc_metals(self, uploaded_file):
        # dbf/maa/maa02.DBF
        table = DBF(uploaded_file)

        data_list = []
        for record in table:
            new_dict = {}
            try:
                new_dict['precious_metals'] = hmodels.PreciousMetals.objects.filter(
                    id=record.get('KM')
                    ).first()
                new_dict['inv_number'] = record.get('INV_N')
                new_dict['metal_amount'] = record.get('MET')
                new_dict['moc_list'] = models.MocList.objects.filter(
                    inv_number=record.get('INV_N')
                    ).first()
                data_list.append(new_dict)
            except (models.MocList.DoesNotExist):
                continue
            except Exception as e:
                error_type = type(e).__name__
                print(f"{error_type}: {e}")
                print(record)

        obj_list = [models.MocMetals(**data_dict) for data_dict in data_list]
        models.MocMetals.objects.bulk_create(obj_list)

    def copy_verification_info(self, uploaded_file):
        # dbf/maa/maa05.DBF
        table = DBF(uploaded_file)

        data_list = []
        for record in table:
            new_dict = {}
            try:
                new_dict['inv_number'] = record.get('INV_N')
                new_dict['entry_date'] = record.get('DAT_POST')
                new_dict['verification_date'] = record.get('DAT_POV')
                new_dict['workshop_issue_date'] = record.get('DAT_VID_V_')
                new_dict['verification_result'] = record.get('REZ')
                new_dict['verification_person'] = hmodels.VerificationPerson.objects.filter(code=record.get('KOD_POV')).first()
                new_dict['verification_sign'] = hmodels.VerificationSign.objects.filter(code=record.get('PR_POV')).first()
                new_dict['verification_document_num'] = record.get('NUMDOC')
                new_dict['moc_list'] = models.MocList.objects.filter(
                    inv_number=record.get('INV_N')
                    ).first()
                data_list.append(new_dict)
            except (models.MocList.DoesNotExist):
                continue
            except Exception as e:
                error_type = type(e).__name__
                print(f"{error_type}: {e}")
                print(record)

        obj_list = [models.VerificationInfo(**data_dict) for data_dict in data_list]
        models.VerificationInfo.objects.bulk_create(obj_list)

    def copy_repair_info(self, uploaded_file):
        # dbf/maa/maa06.DBF
        table = DBF(uploaded_file)

        data_list = []
        for record in table:
            new_dict = {}
            try:
                new_dict['inv_number'] = record.get('INV_N')
                new_dict['entry_date'] = record.get('DAT_POST')
                new_dict['entry_repair_date'] = record.get('DAT_VID_V_')
                new_dict['repair_date'] = record.get('DAT_REM')
                new_dict['repair_type'] = record.get('VID_REM')
                new_dict['repair'] = hmodels.Repair.objects.filter(id=record.get('HAR_REM')).first()
                new_dict['repair_code'] = hmodels.RepairCode.objects.filter(code=record.get('KAT_REM')).first()
                new_dict['repair_department'] = hmodels.RepairDepartment.objects.filter(code=record.get('KOD_REM')).first()
                new_dict['instrument_failure'] = hmodels.InstrumentFailure.objects.filter(code=record.get('PRICH_OTK')).first()
                new_dict['moc_list'] = models.MocList.objects.filter(
                    inv_number=new_dict['inv_number']
                    ).first()
                if new_dict['repair_type'] is None:
                    new_dict['repair_type'] = models.RepairInfo.RepairType.CURRENT
                data_list.append(new_dict)
            except (models.MocList.DoesNotExist):
                print('not found moc_list:' + record)
                continue
            except Exception as e:
                error_type = type(e).__name__
                print(f"{error_type}: {e}")
                print(record)

        obj_list = [models.RepairInfo(**data_dict) for data_dict in data_list]
        models.RepairInfo.objects.bulk_create(obj_list)

    def copy_device_location(self, uploaded_file):
        # dbf/maa/maa07.DBF
        table = DBF(uploaded_file)

        data_list = []
        for record in table:
            new_dict = {}
            try:
                new_dict['inv_number'] = record.get('INV_N')
                new_dict['entry_date'] = record.get('DATV')
                new_dict['department'] = hmodels.Department.objects.filter(workshop=record.get('CEX'), brigade=record.get('BR')).first()
                new_dict['moc_list'] = models.MocList.objects.filter(
                    inv_number=record.get('INV_N')
                    ).first()
                data_list.append(new_dict)
            except (models.MocList.DoesNotExist):
                continue
            except Exception as e:
                error_type = type(e).__name__
                print(f"{error_type}: {e}")
                print(record)
                break

        obj_list = [models.DeviceLocation(**data_dict) for data_dict in data_list]
        models.DeviceLocation.objects.bulk_create(obj_list)

    def copy_device_status(self, uploaded_file):
        # dbf/maa/maa08.DBF
        table = DBF(uploaded_file)

        data_list = []
        for record in table:
            new_dict = {}
            try:
                new_dict['inv_number'] = record.get('INV_N')
                new_dict['status_date'] = record.get('DAT_STAT')
                new_dict['device_status'] = hmodels.DeviceStatus.objects.filter(id=record.get('KOD_STAT')).first()
                new_dict['moc_list'] = models.MocList.objects.filter(
                    inv_number=record.get('INV_N')
                    ).first()
                data_list.append(new_dict)
            except (models.MocList.DoesNotExist):
                continue
            except Exception as e:
                error_type = type(e).__name__
                print(f"{error_type}: {e}")
                print(record)

        obj_list = [models.DeviceStatusDate(**data_dict) for data_dict in data_list]
        models.DeviceStatusDate.objects.bulk_create(obj_list)

    def copy_device_station(self, uploaded_file):
        # dbf/maa/maa09.DBF
        table = DBF(uploaded_file)

        data_list = []
        for record in table:
            new_dict = {}
            try:
                new_dict['inv_number'] = record.get('INVN')
                new_dict['station_inv_number'] = record.get('INVN_ST')
                new_dict['station_name'] = record.get('NAME_ST')
                new_dict['moc_list'] = models.MocList.objects.filter(
                    inv_number=record.get('INVN')
                    ).first()
                data_list.append(new_dict)
            except (models.MocList.DoesNotExist):
                continue
            except Exception as e:
                error_type = type(e).__name__
                print(f"{error_type}: {e}")
                print(record)

        obj_list = [models.DeviceStation(**data_dict) for data_dict in data_list]
        models.DeviceStation.objects.bulk_create(obj_list)
