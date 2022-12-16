//******* PMA/PMO Select *****/

function enablePmaPmo(answer) {
    console.log(answer.value);
    if (answer.value == "pma" ){
        document.getElementById('band_pmo_class').classList.add('d-none');
        document.getElementById('band_pma_class').classList.remove('d-none'); 

    } else if (answer.value == "pmo" ) {
        document.getElementById('band_pma_class').classList.add('d-none');
        document.getElementById('band_pmo_class').classList.remove('d-none');

    } else {
        document.getElementById('band_pma_class').classList.remove('d-none'); 
        document.getElementById('band_pmo_class').classList.remove('d-none');
    }

}



//******* Country Select *****/

// Set up an array of countries, and an object with those
// countries as keys - their values will be whatever you want
// the second select updated with
const countries = ['Select', 'Brazil', 'Canada', 'Mexico', 'SSA', 'United States'];
const options = { brazil: [['Select', 'B4', 'B5', 'B6', 'B7'], ['Select', 'B4', 'B5', 'B6', 'B7']], canada: [['Select', 'B5', 'B6', 'B7'], ['Select', 'B5', 'B6', 'B7']], mexico: [['Select', 'B4', 'B5', 'B6', 'B7'], ['Select', 'B4', 'B5', 'B6', 'B7']], ssa: [['Select', 'B4', 'B5', 'B6', 'B7'], ['Select', 'B4', 'B5', 'B6', 'B7']], usa: [['Select', 'B5', 'B6', 'B7'], ['Select', 'B5', 'B6', 'B7']] };

// Initialise the country
const country = 'Select';

const countriesSelect = document.querySelector('#countries');
const bandPmaSelect = document.querySelector('#bandPma');
const bandPmoSelect = document.querySelector('#bandPmo');

// Add a change listener to the country select
countriesSelect.addEventListener('change', handleChange);

// Initialise the select options
countriesSelect.innerHTML = createOptions(countries);
updatebandPmaSelect(country);

// Get the value from the changed select
function handleChange(e) {
  const { value } = e.target;
  updatebandPmaSelect(value);  
}

// Update the second select with the values from
// the dictionary
function updatebandPmaSelect(value) {
  bandPmaSelect.innerHTML = createOptions(options[value][0]);
  bandPmoSelect.innerHTML = createOptions(options[value][1]);
}

// Create some options
function createOptions(data) {
  return data.map(option => {
    return `
      <option value="${option.toLowerCase()}">
        ${option}
      </option>`;
  });
}



//******* Fields Validation *****/

// function validatefields1() {
//   let x = document.forms["checklistForm"]["user_name"].value;
//   if (x == "") {
//     alert("Name must be filled out");
//     return false;
//   } else{
    
//   }
// }



