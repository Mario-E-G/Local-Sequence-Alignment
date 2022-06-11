let btn1 = document.querySelector("#btn1")
let btn2 = document.querySelector("#btn2")
let sequence = document.querySelector("#sequence")
let textArea1 = document.querySelector("#txt1")
let textArea2 = document.querySelector("#txt2")
let firstSequence = document.querySelector("#first-sequence")
let secondSequence = document.querySelector("#second-sequence")
let file1 = document.querySelector("#file1")
let file2 = document.querySelector("#file2")
let result = document.querySelector(".result")
let submit = document.querySelector("#submit")




function pad1() {
    btn1.style.backgroundColor = "rgb(0, 56, 50)"
}
function Npad1() {
    btn1.style.backgroundColor = "rgb(206, 200, 166)"
}
function pad2() {
    btn2.style.backgroundColor = "rgb(0, 56, 50)"
}
function Npad2() {
    btn2.style.backgroundColor = "rgb(206, 200, 166)"
}
function pad3() {
    submit.style.backgroundColor = "rgb(0, 56, 50)"
}
function Npad3() {
    submit.style.backgroundColor = "rgb(206, 200, 166)"
}
function choiceCheck() {
    if (firstSequence.checked == true) {
        textArea1.value = ""
        // textArea1.Autofocus = true
        textArea1.readOnly = false
        btn1.value = ""
        btn1.disabled = true
    } if (file1.checked == true) {
        textArea1.value = ""
        textArea1.readOnly = true
        btn1.disabled = false
    } if (btn1.value == "") {
        textArea1.value = ""
    }
}
function choiceCheck2() {
    if (secondSequence.checked == true) {
        textArea2.value = ""
        textArea2.readOnly = false
        btn2.value = ""
        btn2.disabled = true
    } if (file2.checked == true) {
        textArea2.value = ""
        textArea2.readOnly = true
        btn2.disabled = false
    } 
}
btn1.addEventListener('change', () => {
    let files = btn1.files;
    if (files.length == 0) return;
    const file = files[0];

    let reader = new FileReader();

    reader.onload = (e) => {
        const file = e.target.result;

        const lines = file.split(/\r\n|\n/);
        textArea1.value = lines.join('\n');
        console.log(textArea1.value)
    };
    reader.onerror = (e) => alert(e.target.error.name);
    reader.readAsText(file);
    console.log(textArea1.value)
});
btn2.addEventListener('change', () => {
    let files = btn2.files;

    if (files.length == 0) return;
    const file = files[0];
    let reader = new FileReader();

    reader.onload = (e) => {
        const file = e.target.result;
        const lines = file.split(/\r\n|\n/);
        textArea2.value = lines.join('\n');

    };

    reader.onerror = (e) => alert(e.target.error.name);
    reader.readAsText(file);
});
// function clearFileInput(id) {
//     var oldInput = document.getElementById(id);

//     var newInput = document.createElement("input");

//     newInput.type = "file";
//     newInput.id = oldInput.id;
//     newInput.name = oldInput.name;
//     newInput.className = oldInput.className;
//     newInput.style.cssText = oldInput.style.cssText;
//     // TODO: copy any other relevant attributes 

//     oldInput.parentNode.replaceChild(newInput, oldInput);
// }