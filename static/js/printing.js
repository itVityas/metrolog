function print_to_html() {
  const modal = new bootstrap.Modal(document.getElementById('modal_window_print'));
  modal.show();
}

function print_to_pdf(){
  const content = document.getElementById('print_container').innerHTML;
  const printWindow = window.open('', '', 'height=600,width=800');
  var prtCSS = '<link rel="stylesheet" href="/static/css/bootstrap.min.css" type="text/css" />';
  const result_html = '<html><head>' + prtCSS + '</head><body>' + content + '</body></html>';
  printWindow.document.write(result_html);
  printWindow.document.close();
  printWindow.focus();
  printWindow.print();
  printWindow.close();
}

async function print_to_word(e){
  const content = document.getElementById('print_container').innerHTML;
  var prtCSS = '<link rel="stylesheet" href="/static/css/bootstrap.min.css" type="text/css" />';
  const result_html = '<html><head>' + prtCSS + '</head><body>' + content + '</body></html>';

  const name = 'document';
  const data = { html_to_print: result_html, name: name };

  const csrfToken = e.children[0].value;
  const response = await fetch("http://127.0.0.1:8000/general/print_to_docx/", {
        method: "POST",
        headers: {
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify(data),
    }).catch(error => console.error('Error fetching data:', error));

    if (!response.ok) throw new Error('Network response failed.');

    // 1. Convert response payload to a Blob object
    const blob = await response.blob();

    // 2. Create a temporary local URL pointing to the Blob
    const blobUrl = window.URL.createObjectURL(blob);

    // 3. Create a hidden <a> element to simulate a click download
    const link = document.createElement('a');
    link.href = blobUrl;
    link.download = name + '.docx'; // Sets the target file name

    // 4. Append to DOM, click it, and clean up immediately
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    // 5. Free up memory allocated to the Blob URL
    window.URL.revokeObjectURL(blobUrl);
}