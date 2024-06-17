<template>
    <div class="container">
        <div class="mainContent">
            <div class="selectedCategories">
                <p><b>Selected Categories: </b></p>
                <span v-if="inputValid" v-for="category in inputCategories" :key="category.name" :style="{ backgroundColor: category.color }">
                    {{ category.name }}
                </span>
            </div>
            <p><b>Text: </b></p>
            <div class="outputText">
                <p v-if="inputValid" v-html="highlightedText" @mouseover="handleMouseOver" @mouseleave="handleMouseLeave"></p>
            </div>
        </div>
        <Sidebar v-if="hoveredSection" :section="hoveredSection" />
    </div>
</template>

<script>
    import axios from 'axios'
    import { categories } from '@/assets/categories';
    import Sidebar from './Sidebar.vue';

    export default {
        name: 'ResultPage',
        components: { Sidebar },
        data() {
            return {
                inputValid: true,
                inputText: this.getInputText(),
                inputCategories: this.getInputCategories(),
                analysis: {},
                hoveredSection: null // Add this data property
            }
        },
        computed: {
            highlightedText() {
                let text = this.inputText;
                if (this.analysis && this.analysis.sections) {
                    this.analysis.sections.forEach(section => {
                        const category = this.inputCategories.find(cat => cat.name == section.category);
                        if (category) {
                            const coloredSpan = `<span class="highlighted" style="background-color: ${category.color};" data-category="${section.category}" data-sub-category="${section['sub_category']}" data-explanation="${section.explanation}">${section.section}</span>`;
                            text = text.replace(section.section, coloredSpan);
                        }
                    });
                }
                return text;
            }
        },
        methods: {
            getInputText() {
                var storedText = localStorage.getItem('CAT_input_text');
                if (storedText)
                    return storedText;
                else
                    this.inputValid = false
            },
            getInputCategories() {
                var storedCategories = localStorage.getItem('CAT_input_categories');
                if (storedCategories) {
                    const selectedCategories = storedCategories.split(',');
                    return categories.filter(category => selectedCategories.includes(category.name));
                } else {
                    this.inputValid = false
                }
            },
            async getAnalysis() {
                // API call
                let categoryNames = this.inputCategories.map(category => category.name);
                this.analysis = (await axios.post("http://localhost:8000/analyse", {"input_text": this.inputText, "input_categories": categoryNames})).data
                console.log("Analysis\n", this.analysis);
            },
            handleMouseOver(event) {
                if (event.target.classList.contains('highlighted')) {
                    this.hoveredSection = {
                        category: event.target.dataset.category,
                        subCategory: event.target.dataset.subCategory,
                        explanation: event.target.dataset.explanation,
                        color: event.target.style.backgroundColor
                    };
                }
            },
            handleMouseLeave() {
                this.hoveredSection = null;
            }
        },
        mounted (){
            this.getAnalysis()
        },
    }
</script>

<style>
.container {
    display: flex;
    flex-direction: row;
    width: 90vw;
    height: 98vh;
}

.mainContent {
    display: flex;
    flex-flow: column wrap;
    width: 70%;
    padding: 2rem;
}

.sidebar {
    display: flex;
    flex-flow: column wrap;
    align-self: flex-end;
    justify-self: flex-end;
    width: 30%;
    background-color: #f4f4f4;
}

.selectedCategories span {
    padding: 5px 10px;
    margin-right: 5px;
    margin-bottom: 1rem;
    border-radius: 5px;
    color: white;
    display: inline-block;
}

.outputText {
    width: 100%;
    max-width: 600px;
    min-height: 30vh;
    margin-bottom: 1.5rem;
    font-family: Helvetica, Avenir, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    padding: 25px;
    border-radius: 25px;
    border: 1px solid #f4f4f4;
    background-color: #fff;
    font-size: 18px;
    line-height: 1.6;
}

.highlighted {
    padding: 3px;
    border-radius: 4px;
    color: #fff;
    display: inline;
    line-height: 1.6;
}
</style>