let in_v = document.querySelectorAll('.js-v');
let in_pn = document.querySelectorAll('.js-pn');
let in_tn = document.querySelectorAll('.js-tn');
let in_zn = document.querySelectorAll('.js-zn');
let in_press_pk = document.querySelectorAll('.js-press_pk');
let in_tk = document.querySelectorAll('.js-tk');
let in_zk = document.querySelectorAll('.js-zk');
let in_v_op = document.querySelectorAll('.js-v_op');
let in_ng_prod = document.querySelectorAll('.js-ng_prod');
let in_ng_nl = document.querySelectorAll('.js-ng_nl');
let in_xg_prod = document.querySelectorAll('.js-xg_prod');
let in_n = document.querySelectorAll('.js-n');
let in_pn_op = document.querySelectorAll('.js-pn_op');
let in_mol = document.querySelectorAll('.js-mol');

for (let i=0; i<in_v.length; i++){
    in_v[i].addEventListener('input',function (){
        calculated_vop(i);
        calculated_pr_op(i);
    });
}
for (let i=0; i<in_pn.length; i++){
    in_pn[i].addEventListener('input',function (){
        calculated_vop(i);
        calculated_pr_op(i);
    });
}
for (let i=0; i<in_tn.length; i++){
    in_tn[i].addEventListener('input',function (){
        calculated_vop(i);
        calculated_pr_op(i);
    });
}
for (let i=0; i<in_zn.length; i++){
    in_zn[i].addEventListener('input',function (){
        calculated_vop(i);
        calculated_pr_op(i);
    });
}
for (let i=0; i<in_press_pk.length; i++){
    in_press_pk[i].addEventListener('input',function (){
        calculated_vop(i);
        calculated_pr_op(i);
    });
}
for (let i=0; i<in_tk.length; i++){
    in_tk[i].addEventListener('input',function (){
        calculated_vop(i);
        calculated_pr_op(i);
    });
}

for (let i=0; i<in_zk.length; i++){
    in_zk[i].addEventListener('input',function (){
        calculated_vop(i);
        calculated_pr_op(i);
    });
}

for (let i=0; i<in_n.length; i++){
    in_n[i].addEventListener('input',function (){
        calculated_vop(i);
        calculated_pr_op(i);
    });
}

for (let i=0; i<in_ng_nl.length; i++){
    in_ng_nl[i].addEventListener('input',function (){
        calculated_xr_prod(i);
        calculated_pr_op(i);
    });
}

for (let i=0; i<in_mol.length; i++){
    in_mol[i].addEventListener('input',function (){
        in_ng_prod[i].value = in_mol[i].value;
        calculated_pr_op(i);
    });
}

function calculated_vop(i){
    in_v_op[i].value = (2893 * Number(in_v[i].value) *
        ((Number(in_pn[i].value) / (Number(in_tn[i].value)*Number(in_zn[i].value))) -
            (Number(in_press_pk[i].value) / (Number(in_tk[i].value) * Number(in_zk[i].value)))) *
            Number(in_n[i].value)).toFixed(3);
}

function calculated_xr_prod(i){
    if (Number(in_ng_nl[i].value) === 0){
        in_xg_prod[i].value = 0;

    }else{
        in_xg_prod[i].value = (Number(input_rtp[i].value) / Number(in_ng_nl[i].value)).toFixed(3);
    }
}

function calculated_pr_op(i){
    in_pn_op[i].value = ((2893 * Number(in_v[i].value) *
        ((Number(in_pn[i].value) / (Number(in_tn[i].value)*Number(in_zn[i].value))) -
            (Number(in_press_pk[i].value) / (Number(in_tk[i].value) * Number(in_zk[i].value)))) *
           Number(in_xg_prod[i].value) * Number(in_n[i].value)) ).toFixed(3);
}