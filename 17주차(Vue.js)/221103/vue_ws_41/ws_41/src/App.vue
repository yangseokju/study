<template>
  <div id="app">
    <h1>버튼 박스 제작</h1>
    <div class="shadow">
      <h2>예약 페이지</h2>
      <h3>시간 선택</h3>
      <div>
        <button v-for="(time, i) in times" :key="i"
        class="selected1" 
        @click="btnclick"
        :class="{'selected2':isSelected1(time)}">{{time}}</button>
      </div>
      <hr>
      <h3>선택 시간 :
      <span v-for="(select, j) in selected" :key="j">
        {{select}}
      </span>
      </h3>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function() {
      return {times: [
        "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
        "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
        "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      selected : [],
      btn:false
    }
  },
  methods: {
    btnclick: function(timedata) {
      const time = timedata.currentTarget.textContent
      if (this.selected.includes(time)) {
        this.selected.splice(this.selected.indexOf(time),1)
      } else {
          if (this.selected.length == 5) {
          alert('5타임까지만 신청할 수 있습니다.')
          } else{
            this.selected.push(time)
          }
      }
    },
    isSelected1: function(timedata) {
      if (this.selected.includes(timedata)) {
        return true
      } else {
        return false
      }
    },
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.shadow {
  box-shadow: 10px 10px 10px 10px #e3e3e3;
}


.selected1:hover{
  color : #0F4c81;
  background-color: #658dc63d;
}


.selected1 {
  color : #838383;
  background-color: rgba(0,0,0,0);
  border : 1px solid rgba(0,0,0,0);
  padding : 8px;
}

.selected2 {
  color : #838383;
  border: 1px solid rgb(58, 143, 182);
  background-color: rgb(185, 226, 245);
  padding : 8px;
}

</style>