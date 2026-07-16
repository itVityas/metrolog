function print_to_html() {
  const modal = new bootstrap.Modal(document.getElementById('modal_window_print'));
  modal.show();
}
  var pdfStyles = `
    <style>
      @page {
        size: A4;
        margin: 20mm 15mm 25mm 15mm; /* Немного увеличили нижний отступ (25mm) для номера */
        
        /* Настройка нижнего колонтитула по центру */
        @bottom-center {
          content: "Страница " counter(page) " из " counter(pages);
          font-family: 'Times New Roman' !important;
          font-size: 10pt !important;
          color: #555555;
        }
      }

      /* Фиксируем адекватный размер шрифта для всего документа */
      html, body {
        font-family: 'Times New Roman' !important;
        font-size: 12pt !important;
        line-height: 1.4 !important;
        color: #000000 !important;
        width: 100% !important;
      }
      h1, h2, h3, h4, h5, p {
        font-family: 'Times New Roman' !important;
        font-size: 12pt !important;
      }
      /* Жестко укрощаем таблицу Bootstrap 5 */
      table.table {
        display: table !important;
        max-width: 100% !important;
        table-layout: auto !important;
        border-collapse: collapse !important;
        margin-top: 10px !important;
      }
      /* Сбрасываем внутренние свойства ячеек Bootstrap 5 */
      .table > :not(caption) > * > * {
        width: max-content !important;
        font-size: 11pt !important;
        padding: 8px 4px !important;
        white-space: pre-wrap !important;
     /* overflow-wrap: break-word !important;
        word-wrap: break-word !important;
        word-break: break-word !important; */
      }
      table.table td, table.table th {
        word-break: normal !important;
        white-space: pre-wrap !important;
        vertical-align: middle !important;
      }
      table.table tr {
        page-break-inside: avoid !important;
        break-inside: avoid !important;
      }
      .pdf-block {
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        margin-bottom: 20px !important; /* Вместо тега <br> используем аккуратный отступ */
      }
    </style>
  `;
async function print_to_pdf2(e){
  loading_start();
  const content = document.getElementById('print_container').innerHTML;
  
  // 1. Подключаем Bootstrap
  var prtCSS = '<link rel="stylesheet" href="/static/css/bootstrap.min.css" type="text/css" />';
  
  // 2. Добавляем жесткие стили сброса прямо в отправляемый HTML


  // 3. Формируем валидный HTML (ОБЯЗАТЕЛЬНО добавляем мета-тег UTF-8)
  const result_html = '<!DOCTYPE html><html><head><meta charset="UTF-8">' + prtCSS + pdfStyles + '</head><body>' + content + '</body></html>';

  const name = 'document';
  const data = { html_to_print: result_html, name: name };

  // Поиск CSRF токена (исправлен селектор для надежности)
  const csrfToken = e.querySelector('[name=csrfmiddlewaretoken]') ? e.querySelector('[name=csrfmiddlewaretoken]').value : e.children[0].value;
  
  try {
    const response = await fetch("http://127.0.0.1:8000/general/print_to_pdf/", {
          method: "POST",
          headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': csrfToken
          },
          body: JSON.stringify(data),
      });

      if (!response.ok) throw new Error('Network response failed.');

      const blob = await response.blob();
      const fileURL = URL.createObjectURL(blob);
      loding_end();
      window.open(fileURL, '_blank');
  } catch (error) {
      console.error('Error fetching data:', error);
  }
}

async function print_to_word2(e) {
  loading_start();
  const content = document.getElementById('print_container').innerHTML;
  
  // 1. Подключаем Bootstrap
  var prtCSS = '<link rel="stylesheet" href="/static/css/bootstrap.min.css" type="text/css" />';
  
  // 2. Добавляем жесткие стили сброса прямо в отправляемый HTML

  // 3. Формируем валидный HTML (ОБЯЗАТЕЛЬНО добавляем мета-тег UTF-8)
  const result_html = '<!DOCTYPE html><html><head><meta charset="UTF-8">' + prtCSS + pdfStyles + '</head><body>' + content + '</body></html>';

  const name = 'document';
  const data = { html_to_print: result_html, name: name };

  // Поиск CSRF токена (исправлен селектор для надежности)
  const csrfToken = e.querySelector('[name=csrfmiddlewaretoken]') ? e.querySelector('[name=csrfmiddlewaretoken]').value : e.children[0].value;
  
  try {
    const response = await fetch("http://127.0.0.1:8000/general/print_to_docx/", {
          method: "POST",
          headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': csrfToken
          },
          body: JSON.stringify(data),
      });

    if (!response.ok) throw new Error('Network response failed.');

    loding_end();
    // 1. Convert response payload to a Blob object
    const blob = await response.blob();

    // 2. Create a temporary local URL pointing to the Blob
    const blobUrl = window.URL.createObjectURL(blob);
    save_file(blob);


    // 5. Free up memory allocated to the Blob URL
    window.URL.revokeObjectURL(blobUrl);
  } catch (error) {
      console.error('Error fetching data:', error);
  }
}

async function save_file(blob) {
  try {
    const options = {
      suggestedName: 'Document.docx',
      types: [{
        description: 'Microsoft Word Document',
        accept: {
          'application/vnd.openxmlformats-officedocument.wordprocessingml.document': ['.docx']
        }
      }],
      excludeAcceptAllOption: true
    };

    const fileHandle = await window.showSaveFilePicker(options);

    const writableStream = await fileHandle.createWritable();
    await writableStream.write(blob);
    await writableStream.close();
  } catch (error) {
    console.error("Save process failed or aborted:", error.name, error.message);
  }
}