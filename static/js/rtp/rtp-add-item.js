let itemsForm = document.querySelectorAll(".items-form");
let container = document.querySelector("#items-form-container");
let addButton = document.querySelector("#add-item");
let deleteButton =document.querySelector("#delete-item")
let totalForms = document.querySelector("#id_form-TOTAL_FORMS");

let formNum = itemsForm.length-1;

addButton.addEventListener('click', addForm);

function addForm(e){
    e.preventDefault();

    let newForm = itemsForm[0].cloneNode(true);
    let formRegex = RegExp(`form-(\\d){1}-`,'g');

    formNum++;
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`);
    container.insertBefore(newForm, itemsForm[formNum]);

    totalForms.setAttribute('value', `${formNum+1}`);
}

deleteButton.addEventListener('click', deleteForm);

function deleteForm(e){
    e.preventDefault()
    let itemsForm = document.querySelectorAll(".items-form");

    container.removeChild(itemsForm[formNum]);
    formNum--;
    totalForms.setAttribute('value', `${formNum}`);
}


