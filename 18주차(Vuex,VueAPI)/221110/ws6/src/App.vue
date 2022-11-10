<template>
  <div id="app" class="row" style="width:100%;">
    <div class="gogo col-3 m-2 p-2" style="">
      <SideBar/>
    </div>
    <div class="gogo1 col-8 m-2 p-2" style= "">
      <router-view/>
    </div>
  </div>
</template>

<script>
import SideBar from '@/components/SideBar'

export default {
  components: {
    SideBar,
  }
}

</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}

nav {
  padding: 30px;
  margin: auto;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.gogo {
  /* text-align: center; */
  border: 2px solid black;
  border-radius: 10px 10px 10px 10px;
  /* display: flex; */
  /* justify-content: center;
  align-items: center; */
}

.gogo1 {
  border: 2px solid black;
  border-radius: 10px 10px 10px 10px;
  /* display: flex; */
  /* justify-content: center;
  align-items: center; */
}
</style>
