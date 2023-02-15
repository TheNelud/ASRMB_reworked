function calculated() {
    let in_v_pr = document.querySelectorAll('.js-v_pr');
    let in_p_pr = document.querySelectorAll('.js-p_pr');
    let in_t_pr = document.querySelectorAll('.js-t_pr');
    let in_z_pr = document.querySelectorAll('.js-z_pr');
    let in_b = document.querySelectorAll('.js-b');
    let in_ni = document.querySelectorAll('.js-ni');
    let in_xr_prod = document.querySelectorAll('.js-xr_prod');
    let in_pr_op = document.querySelectorAll('.js-pr_op');
    let in_v_p = document.querySelectorAll('.js-v_p');
    let in_tau = document.querySelectorAll('.js-tau');
    let in_xrr_prod = document.querySelectorAll('.js-xrr_prod');
    let in_n = document.querySelectorAll('.js-n');
    let in_pr_pot = document.querySelectorAll('.js-pr_pot');
    let in_pr_pr = document.querySelectorAll('.js-pr_pr');

    for(let i=0; i<in_v_pr.length; i++){
        in_v_pr[i].addEventListener('input', function (){
            console.log(in_v_pr[i].value);calc_pr_op(i);
        });
    }
    for(let i=0; i<in_p_pr.length; i++){
        in_p_pr[i].addEventListener('input', function (){
            console.log(in_p_pr[i].value);calc_pr_op(i);
        });
    }
    for(let i=0; i<in_t_pr.length; i++){
        in_t_pr[i].addEventListener('input', function (){
            console.log(in_t_pr[i].value);calc_pr_op(i);
        });
    }
    for(let i=0; i<in_z_pr.length; i++){
        in_z_pr[i].addEventListener('input', function (){
            console.log(in_z_pr[i].value);calc_pr_op(i);
        });
    }
    for(let i=0; i<in_b.length; i++){
        in_b[i].addEventListener('input', function (){
            console.log(in_b[i].value);calc_pr_op(i);
        });
    }
    for(let i=0; i<in_ni.length; i++){
        in_ni[i].addEventListener('input', function (){
            console.log(in_ni[i].value);calc_pr_op(i);
        });
    }
    for(let i=0; i<in_xr_prod.length; i++){
        in_xr_prod[i].addEventListener('input', function (){
            console.log(in_xr_prod[i].value);calc_pr_op(i);
        });
    }

    function calc_pr_op(i){
        if (Number(in_t_pr[i].value) === 0 || Number(in_z_pr[i].value) ===0){
            in_pr_op[i].value = 0;
        }else{
            in_pr_op[i].value = (2893 * (Number(in_v_pr[i].value)* Number(in_p_pr[i].value)/Number(in_t_pr[i].value)/Number(in_z_pr[i].value))
                * (Number(in_b[i].value) + 1) * Number(in_ni[i].value) * Number(in_xr_prod[i].value)).toFixed(3);
        }
    }


}

calculated();


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
    calculated();

}

deleteButton.addEventListener('click', deleteForm);

function deleteForm(e){
    e.preventDefault()
    let itemsForm = document.querySelectorAll(".items-form");

    container.removeChild(itemsForm[formNum]);
    formNum--;
    totalForms.setAttribute('value', `${formNum}`);
}