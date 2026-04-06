function print_to_html(divId) {
  const content = document.getElementById(divId).innerHTML;
  const printWindow = window.open('', '', 'height=600,width=800');
  printWindow.document.write('<html><body>' + content + '</body></html>');
  printWindow.document.close();
  printWindow.print();
}