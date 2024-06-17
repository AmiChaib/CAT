<template>
    <div class="sidebar" :style="{ backgroundColor: section.color }">
        <h1 v-if="section.category">{{ section.category }}</h1>
        <h2 v-if="section.subCategory">{{ section.subCategory }}</h2>
        <p v-if="section.explanation">{{ section.explanation }}</p>
    </div>
</template>

<script>
export default {
    name: 'Sidebar',
    props: {
        section: {
            type: Object,
            required: true
        }
    }
}
</script>

<style scoped>
.sidebar {
    display: flex;
    flex-flow: column wrap;
    height: 100%;
    padding: 2rem;
    background-color: #f4f4f4;
    box-sizing: border-box;
    border-radius: 25px;
    width: 35%;
}
</style>