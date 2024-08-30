function onClick(button) {
    var codeBlock = button.parentNode;

    var tempInput = document.createElement("textarea");
    tempInput.value = codeBlock.querySelector("pre code").textContent;
    document.body.appendChild(tempInput);

    tempInput.select();

    document.execCommand("copy");

    document.body.removeChild(tempInput);

    alert("Код скопирован!");
}
