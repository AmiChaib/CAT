<template>
  <router-view/>
</template>

<style>
#app {
  font-family: Helvetica, Avenir, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-weight: lighter;
  text-align: center;
  color: #2c3e50;
  display: flex;
  flex-flow: column wrap;
  width: 95%;
  justify-content: center;
  align-content: center;
  justify-items: center;
  align-items: center;
  text-align: left;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
