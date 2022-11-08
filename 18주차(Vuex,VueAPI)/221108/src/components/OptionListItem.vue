<template>
  <div style="background-color:gainsboro; width:100%; padding:15.05%; border: 1px solid black">
    <div style="float:left">
      {{ option.type }}
    </div>
    <div style="float:right">
      <button @click="decrease">-</button>
      {{ option.count }}
      <button @click="increase">+</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OptionListItem',
  props: {
    option: Object,
  },
  methods: {
    increase() {
      this.$store.dispatch("increase", {option:this.option, flag:1})
    },
    decrease() {
      this.$store.dispatch("decrease", {option:this.option, flag:2})
    },
  },
}
</script>

<style>

.is-selected {
  background-color : greenyellow;
}

</style>