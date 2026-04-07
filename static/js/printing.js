function print_to_html() {
  const content = document.getElementById('print_container').innerHTML;
  const printWindow = window.open('', '', 'height=600,width=800');
  var prtCSS = '<link rel="stylesheet" href="/static/css/bootstrap.min.css" type="text/css" />';
  printWindow.document.write('<html><head>' + prtCSS + '</head><body>' + content + '</body></html>');
  printWindow.document.close();
  printWindow.focus();
  printWindow.print();
  printWindow.close();
}