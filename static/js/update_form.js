
document.querySelectorAll('.modal:has(form)').forEach(function(modalElement) {
  modalElement.addEventListener('hide.bs.modal', function (e) {
    if (!confirm('Вы уверены, что хотите закрыть окно? Несохраненные изменения будут потеряны.')) {
      e.preventDefault();
    }
  });
});
// Отслеживаем открытие ЛЮБОГО модального окна на странице
document.addEventListener('show.bs.modal', function (event) {
  const openingModal = event.target; // Окно, которое открывается прямо сейчас

  // Ищем уже открытые модальные окна, кроме текущего
  const openModals = Array.from(document.querySelectorAll('.modal.show'))
    .filter(modal => modal !== openingModal);

  // Если нашли открытое окно (оно стало "задним")
  if (openModals.length > 0) {
    // Берем самое последнее открытое окно
    const activeBackModal = openModals[openModals.length - 1];
    
    // Добавляем ему класс размытия
    activeBackModal.classList.add('blur-sibling');
    
    // Привязываем событие закрытия к НОВОМУ окну, чтобы убрать размытие со СТАРОГО
    openingModal.addEventListener('hidden.bs.modal', function onClose() {
      activeBackModal.classList.remove('blur-sibling');
      // Удаляем этот временный обработчик, чтобы не копились утечки памяти
      openingModal.removeEventListener('hidden.bs.modal', onClose);
    });
  }
});

function fill_modal_window(e) {
    const modal = new bootstrap.Modal(document.getElementById("modal_window_add"));
    const form = document.getElementById("modal_form");

    const row = e.parentElement.parentElement;
    const cells = row.children;

    for(const [index, cell] of [...cells].entries()){
        if (index === cells.length - 2) {
            break;
        }
        if (index === 0) {
            continue;
        }
        switch ([...form.elements][index].type){
            case "checkbox":
                [...form.elements][index].checked = (cell.textContent === "Да") ? true : false;
                break;
            case "number":
                [...form.elements][index].value = (cell.textContent.includes(',')) ? parseFloat(cell.textContent.replace(',','.')) : parseInt(cell.textContent);
                break;
            default:
                [...form.elements][index].value = cell.textContent;
        }

    }

    const id = cells[0].textContent;
    form_id_input = form.elements["id"];
    form_id_input.value = id;

    form.action = "" + id + "/update/";
    modal.show();
};

function flush_modal_window(e) {
    const modal = new bootstrap.Modal(document.getElementById("modal_window_add"));
    const form = document.getElementById("modal_form");

    form.reset();
    form.action = "add/";
    modal.show();
}

function show_delete_modal(e){
    const modal_delete = new bootstrap.Modal(document.getElementById("modal_window_delete"));
    const delete_button = document.getElementById("delete_button");

    const row = e.parentElement.parentElement;
    const cells = row.children;

    const id = cells[0].textContent;

    delete_button.data = id;
    modal_delete.show();
}

function makedelete(e){
    const csrfToken = e.children[0].value;
    fetch("" + e.data + "/delete/", {
        method: "DELETE",
        headers: {
            'X-CSRFToken': csrfToken
        },
    }).then(response => {
        response.text().then(text =>{
            console.log(text)
            document.open()
            document.write(text)
            document.close()
        })
    })
    .catch(error => console.error('Error fetching data:', error));
}


function show_table(e, id_show){
    const tables = document.getElementById("table_container").children;
    const buttons = document.getElementById("buttons_container").children[0].children;

    for (var i = 0; i < buttons.length; i++) {
        buttons[i].classList.remove('btn-light');
        buttons[i].classList.add('btn-primary-outline');
    }
    e.classList.remove('btn-primary-outline');
    e.classList.add('btn-light');

    for (var i = 0; i < tables.length; i++) {
        if(tables[i].id === id_show){
            tables[i].classList.remove('d-none');
        }else{
            tables[i].classList.add('d-none');
        }
    }
}

function fill_modal_moc_list(e) {
    const modal = new bootstrap.Modal(document.getElementById("modal_window_add"));
    const form = document.getElementById("modal_form");

    const moc_group_name = document.getElementById("moc_group_name").getAttribute('value');
    const moc_type_type = document.getElementById("moc_type_type").getAttribute('value');
    const factory_number = document.getElementById("factory_number").textContent;
    const inv_number = document.getElementById("inv_number").textContent;
    const verification_type = document.getElementById("verification_type").textContent;
    const verification_period = document.getElementById("verification_period").textContent;
    const verification_department_name = document.getElementById("verification_department_name").getAttribute('value');
    const change_type_name = document.getElementById("change_type_name").getAttribute('value');
    const sign_o_m = document.getElementById("sign_o_m").textContent;
    const sign_o_r = document.getElementById("sign_o_r").textContent;

    form.elements['moc_group'].value = moc_group_name
    form.elements['moc_type'].value = moc_type_type
    form.elements['factory_number'].value = factory_number
    form.elements['inv_number'].value = inv_number
    form.elements['verification_type'].value = verification_type
    form.elements['verification_period'].value = verification_period
    form.elements['verification_department'].value = verification_department_name
    form.elements['change_type'].value = change_type_name
    form.elements['sign_o_m'].value = sign_o_m
    form.elements['sign_o_r'].value = sign_o_r

    const id = document.getElementById("main_container").getAttribute('value');
    console.log(id)
    form.action = "update/";
    modal.show();
};

function show_delete_moc_list(e){
    const modal_delete = new bootstrap.Modal(document.getElementById("modal_window_delete"));
    const delete_button = document.getElementById("delete_button");

    const id = document.getElementById("main_container").getAttribute('value');
    console.log(id)
    delete_button.data = id;
    modal_delete.show();
};

function delete_moc_list(e){
    const csrfToken = e.children[0].value;
    fetch("delete/", {
        method: "DELETE",
        redirect: 'follow',
        headers: {
            'X-CSRFToken': csrfToken
        },
    }).then(response => {
        if (response.redirected) {
            window.location.href = response.url;
        }
    })
    .catch(error => console.error('Error fetching data:', error));
};

function flush_modal_window_table(e, name) {
    const modal = new bootstrap.Modal(document.getElementById("modal_window_add_table"));
    const form = document.getElementById("modal_form_table_"+name);
    const form_collection = document.getElementById("modal_form_collection").children;

    open_form_table(form, form_collection);
    form.reset();
    setInitial(form);
    form.action = name+"/add/";
    modal.show();
};

function open_form_table(form, form_collection){
    for (var i = 0; i < form_collection.length; i++) {
        form_collection[i].classList.add('d-none');
    }
    form.classList.remove('d-none');
};

function setInitial(form){
    // get form elements
    form_inv_number = form.querySelector('#id_inv_number');
    form_moc_list = form.querySelector('#id_moc_list');

    // get values from page
    inv_number = document.getElementById('inv_number').innerText;
    moc_list = document.getElementById('main_container').getAttribute('value');
    
    // set form elements values
    form_inv_number.value = inv_number;
    form_moc_list.value = moc_list;

    form_inv_number.readOnly = true;
}

function fill_modal_window_table(e, name) {
    const modal = new bootstrap.Modal(document.getElementById("modal_window_add_table"));
    const form = document.getElementById("modal_form_table_"+name);
    const form_collection = document.getElementById("modal_form_collection").children;
    
    const row = e.parentElement.parentElement;
    const cells = row.children;

    for(const [index, cell] of [...cells].entries()){
        if (index === cells.length - 2) {
            break;
        }
        form_element = form.querySelector('#id_'+cell.id);
        if(form_element != null){
            console.log(form_element.type)
            switch (form_element.type){
            case "checkbox":
                form_element.checked = (cell.textContent === "Да") ? true : false;
                break;
            case "number":
                form_element.value = (cell.textContent.includes(',')) ? parseFloat(cell.textContent.replace(',','.')) : parseInt(cell.textContent);
                break;
            case "select-one":
                 for (var i = 0; i < form_element.children.length; i++) {
                    console.log(form_element.children[i].innerText)
                    if(form_element.children[i].innerText === cell.textContent){
                        form_element.value = form_element.children[i].getAttribute('value');
                    }
                }
                break;
            default:
                form_element.value = cell.textContent;
            }
        }
        
    }
    setInitial(form);
    open_form_table(form, form_collection);
    const id = cells[0].parentElement.getAttribute('value');
    form.action = "" + name + "/" + id + "/update/";
    modal.show();
};

function show_delete_table(e, name, id){
    const modal_delete = new bootstrap.Modal(document.getElementById("modal_window_delete_table"));
    const delete_button = document.getElementById("delete_button_table");

    delete_button.data = `${name}/${id}`;
    modal_delete.show();
};

function delete_table(e){
    const csrfToken = e.children[0].value;
    fetch("" + e.data + "/delete/", {
        method: "DELETE",
        redirect: 'follow',
        headers: {
            'X-CSRFToken': csrfToken
        },
    }).then(response => {
        if (response.redirected) {
            window.location.href = response.url;
        }
    })
    .catch(error => console.error('Error fetching data:', error));
};

function show_modal_in_generic(e, name){
    const modal = new bootstrap.Modal(document.getElementById(name + '_modal'));

    modal.show();
};

function show_modal_in_passport(e, name){
    const modal = new bootstrap.Modal(document.getElementById(name + '_modal'));

    modal.show();
};

function close_modal_in_passport(e, name){
    const modal = bootstrap.Modal.getInstance(document.getElementById(name + '_modal'));

    insert_form(e);
    modal.hide();
};

function loading_start(){
    var loader = document.getElementById('loader-wrapper');
    loader.style.display = 'flex';
}

function loding_end(){
    var loader = document.getElementById('loader-wrapper');
    loader.style.display = 'none';
}

var saved_form = {
    'form_id': '',
    'fields': []
};

function save_form(e){
    form = e.parentElement.parentElement.parentElement.parentElement.parentElement;
    const inputs = form.querySelectorAll("input, select, textarea");
    let temp_array = [];
    inputs.forEach(sourceField => {
        // Only map if the field has a name attribute
        if (sourceField.name && sourceField.name!="csrfmiddlewaretoken") {
            temp_array.push({
                'field_name': sourceField.name,
                'field_value': sourceField.value
            })
        }
    });
    saved_form.form_id = form.getAttribute('id');
    saved_form.fields = temp_array;
    console.log(saved_form);
}

function insert_form(e){
    form = document.getElementById(saved_form.form_id);
    const inputs = form.querySelectorAll("input, select, textarea");

    saved_form.fields.forEach(sourceField => {
        const targetField = form.querySelector(`[name="${sourceField.field_name}"]`);
        if (targetField) {
            targetField.value = sourceField.field_value;
        }
    });
    saved_form.form_id = '';
    saved_form.fields = [];
}
