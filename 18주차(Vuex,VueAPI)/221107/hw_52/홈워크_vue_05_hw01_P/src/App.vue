// App.vue

<template>
  <div id="app">
    <p>Counter: {{ this.$store.state.counter }}</p>
    <p>Counter x2: {{ counterDouble }}</p>
    <p></p>
    <button @click="increase">increase +</button>
    <button @click="decrease">decrease -</button>
  </div>
</template>

<script>
export default {
  name: 'App', 
  data: function() {
    return {
      counter: 0,
    }
  },
  methods: {
    increase() {
      this.$store.dispatch('increase')
    },
    decrease () {
      this.$store.dispatch('decrease')
    },
  },
  computed: {
    counterDouble() {
      return this.$store.getters.counterdouble
    },
  },
}
</script>

<style>
</style>