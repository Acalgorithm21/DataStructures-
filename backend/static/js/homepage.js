const editor = CodeMirror.fromTextArea(
  document.getElementById("editor"),
  {
    mode: "htmlmixed",
    lineNumbers: true,
    tabSize: 2,
  }
);