<template>
  <div>
    <nav>
    <router-link to="/" style="text-decoration:none"><h1>전체</h1></router-link>
    <br>
    <router-link to="/today" style="text-decoration:none"><h1>오늘</h1></router-link>
    <br>
    <router-link to="/important" style="text-decoration:none"><h1>중요</h1></router-link>
    </nav>
  </div>
</template>

<script>

export default {
    name: 'SideBar',
    component: {
    
    },
}
</script>

<style>

</style>