


//MOLAR_CONTENT_OF_COMPONENTS
let sum_molar_content_of_components  = document.getElementById('id_form-11-molar_content_of_components');
let small_molar_content_of_components = document.querySelectorAll('.item_js_molar_content_of_components');
let numbers_molar_content_of_components = [];
for (let i = 0; i < small_molar_content_of_components.length; i++){
    numbers_molar_content_of_components.push(small_molar_content_of_components[i].value);
    small_molar_content_of_components[i].addEventListener('input', function (){
        numbers_molar_content_of_components[i] = this.value;
        updateResults_molar_content_of_components();});
}

updateResults_molar_content_of_components();
function updateResults_molar_content_of_components(){
    sum_molar_content_of_components.value = sumArr_molar_content_of_components(numbers_molar_content_of_components);
}

function sumArr_molar_content_of_components(arr){
    let x = 0;
  for( let i = 0; i < arr.length; i++ ){
    x += +arr[i]; // (*2)
  }
  return x;
}

//MOLAR_MASS_OF_THE_COMPONENT
let sum_molar_mass_of_the_component  = document.getElementById('id_form-11-molar_mass_of_the_component');
let small_molar_mass_of_the_component = document.querySelectorAll('.item_js_molar_mass_of_the_component');
let numbers_molar_mass_of_the_component = [];
for (let i = 0; i < small_molar_mass_of_the_component.length; i++){
    numbers_molar_mass_of_the_component.push(small_molar_mass_of_the_component[i].value);
    small_molar_mass_of_the_component[i].addEventListener('input', function (){
        numbers_molar_mass_of_the_component[i] = this.value;
        updateResults_molar_mass_of_the_component();});
}

updateResults_molar_mass_of_the_component();
function updateResults_molar_mass_of_the_component(){
    sum_molar_mass_of_the_component.value = sumArr_molar_mass_of_the_component(numbers_molar_mass_of_the_component);
}

function sumArr_molar_mass_of_the_component(arr){
    let x = 0;
  for( let i = 0; i < arr.length; i++ ){
    x += +arr[i]; // (*2)
  }
  return x;
}

//total_molar_mass
let sum_total_molar_mass  = document.getElementById('id_form-11-total_molar_mass');
let small_total_molar_mass = document.querySelectorAll('.item_js_total_molar_mass');
let numbers_total_molar_mass = []
for (let i = 0; i < small_total_molar_mass.length; i++){
    numbers_total_molar_mass.push(small_total_molar_mass[i].value);
    small_total_molar_mass[i].addEventListener('input', function (){
        numbers_total_molar_mass[i] = this.value;
        updateResults_total_molar_mass();});
}

updateResults_total_molar_mass();
function updateResults_total_molar_mass(){
    sum_total_molar_mass.value = sumArr_total_molar_mass(numbers_total_molar_mass);
}

function sumArr_total_molar_mass(arr){
    let x = 0;
  for( let i = 0; i < arr.length; i++ ){
    x += +arr[i]; // (*2)
  }
  return x;
}


//chromatograph_mass
let sum_chromatograph_mass  = document.getElementById('id_form-11-chromatograph_mass');
let small_chromatograph_mass = document.querySelectorAll('.item_js_chromatograph_mass');
let numbers_chromatograph_mass = []
for (let i = 0; i < small_chromatograph_mass.length; i++){
    numbers_chromatograph_mass.push(small_chromatograph_mass[i].value);
    small_chromatograph_mass[i].addEventListener('input', function (){
        numbers_chromatograph_mass[i] = this.value;
        updateResults_chromatograph_mass();});
}

updateResults_chromatograph_mass();
function updateResults_chromatograph_mass(){
    sum_chromatograph_mass.value = sumArr_chromatograph_mass(numbers_chromatograph_mass);
}

function sumArr_chromatograph_mass(arr){
    let x = 0;
  for( let i = 0; i < arr.length; i++ ){
    x += +arr[i]; // (*2)
  }
  return x;
}

//chromatograph_mass
let sum_calculated_mass = document.getElementById('id_form-11-calculated_mass');
let small_calculated_mass = document.querySelectorAll('.item_js_calculated_mass');
let numbers_calculated_mass = []
for (let i = 0; i < small_calculated_mass.length; i++){
    numbers_calculated_mass.push(small_calculated_mass[i].value);
    small_calculated_mass[i].addEventListener('input', function (){
        numbers_calculated_mass[i] = this.value;
        updateResults_calculated_mass();});
}

updateResults_calculated_mass();
function updateResults_calculated_mass(){
    sum_calculated_mass.value = sumArr_calculated_mass(numbers_calculated_mass);
}

function sumArr_calculated_mass(arr){
    let x = 0;
  for( let i = 0; i < arr.length; i++ ){
    x += +arr[i]; // (*2)
  }
  return x;
}