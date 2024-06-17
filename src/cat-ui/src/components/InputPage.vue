<template>
    <form @submit.prevent="handleSubmit">
        <p class="checkboxesHeader">Select categories to analyse:</p>
        <!-- Make Error Component instead-->
        <div class="error" v-if="categoriesLengthError">{{ categoriesLengthError }}</div>
        <div class="checkboxesContainer" v-for="checkbox in checkboxes" :key="checkbox.name">
            <label class="checkbox-label" :for="checkbox.name">
                <input 
                    class="checkbox" 
                    type="checkbox" 
                    :id="checkbox.name" 
                    :value="checkbox.name" 
                    v-model="selected_categories" 
                    @change="removeCategoriesLengthError"
                    :style="getCheckboxStyle(checkbox)"
                />
                <p class="checkboxDescription">{{ checkbox.name }}</p>
            </label>
        </div>
        <div class="space"></div>
        <!-- Make Error Component instead-->
        <div class="error" v-if="inputTextLengthError">{{ inputTextLengthError }}</div>
        <textarea placeholder="Insert your text ..." v-model="inputText"></textarea>
        <div class="submit">
            <button class="submit-button">Submit</button>
        </div>
    </form>
</template>

<script>
import { categories } from '@/assets/categories';

export default {
    name: 'InputPage',
    data() {
        return {
            inputText: '',
            checkboxes: categories,
            selected_categories: [],
            inputTextLengthError: '',
            categoriesLengthError: ''
        }
    },
    methods: {
        handleSubmit() {
            this.validateInputs()
            if (this.inputTextLengthError || this.categoriesLengthError)
                return;
            // Save variables globally accessible
            localStorage.setItem('CAT_input_text', this.inputText)
            localStorage.setItem('CAT_input_categories', this.selected_categories)
            // Navigate to result page
            this.$router.push({ path: '/result' })
        },
        validateInputs() {
            // Validate length & content of textarea
            var inputTextLength = this.inputText.length
            if (inputTextLength > 1500)
                this.inputTextLengthError = 'The text is too long. Limit it to 1500 characters, about 250 words.'
            else if (inputTextLength < 30)
                this.inputTextLengthError = 'We need at least a sentence to analyse.'
            // Validate checkboxes (at least 1 checked)
            var categoriesLength = this.selected_categories.length
            if (categoriesLength < 1)
                this.categoriesLengthError = 'Select at least one category to analyse'
        },
        removeCategoriesLengthError() {
            this.categoriesLengthError = ''
        },
        removeInputTextLengthError() {
            this.inputTextLengthError = ''
        },
        getCheckboxStyle(checkbox) {
            const isChecked = this.selected_categories.includes(checkbox.name);
            return {
                backgroundColor: isChecked ? checkbox.color : '#fff',
                border: `2px solid ${checkbox.color}`
            }
        }
    }
}
</script>

<style>
form {
    display: flex;
    flex-flow: column wrap;
    width: 50%;
    justify-self: center;
    margin-top: 1rem;
}
.submit {
    text-align: right;
}
.error {
    padding: 10px;
    border-radius: 15px;
    background-color: #B00020;
    color: white;
    margin-bottom: 5px;
}
.checkboxesContainer {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    margin-left: 20px;
}
.checkbox-label {
    padding: 5px;
    display: flex;
    align-items: center;
    margin-right: 10px;
}
.space {
    width: 99%;
    margin-bottom: 1.5rem;
}
textarea {
    width: 99%;
    height: 30vh;
    margin-bottom: 1.5rem;
    font-family: Helvetica, Avenir, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    padding: 25px;
    border-radius: 25px;
    border: 1px solid #c4c4c4;
    background-color: #fff;
    font-size: 16px;
    resize: none;
}
button {
    width: 15%;
    padding: 10px;
    border-radius: 15px;
}
input[type="checkbox"] {
    -webkit-appearance: none;
    appearance: none;
    background-color: #fff;
    border: 2px solid #000;
    padding: 10px;
    border-radius: 3px;
    display: inline-block;
    position: relative;
    cursor: pointer;
    margin-right: 10px;
    width: 35px;
    height: 35px;
}
input[type="checkbox"]:checked {
    background-color: #000;
}
</style>
