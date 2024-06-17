<template>
    <h1>Critical Text Analysis Tool</h1>
    <div class="instructions"></div>
    <button @click="navigateToInputPage">Start Here</button>
</template>

<script>
    export default {
        name: 'Home',
        methods: {
            navigateToInputPage(){
                this.$router.push('/input')
            }
        }
    }
</script>


<style scoped>
    h1{
        color: rgb(140, 208, 185);
    }
</style>