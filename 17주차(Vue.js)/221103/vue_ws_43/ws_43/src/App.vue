<template>
  <div id="app">
    <h1>SSAFY 상담 예약 시스템</h1>
    <div style="width:auto; height:570px;">
      <TimeTable @from-parent1="fromParent1" @from-parent2="fromParent2"/>
      <MyList :teacher-selected="teacherSelected" :time-selected="timeSelected"/>
    </div>
  </div>
</template>

<script>
import TimeTable from '@/components/TimeTable'
import MyList from '@/components/MyList'

export default {
    name: "App",
    components: {
      TimeTable,
      MyList
    },
    data() {
      return {
        teacherSelected:[],
        timeSelected:[]
      }
    },
    methods: {
      fromParent1(pd) {
        this.teacherSelected = pd
      },
      fromParent2(pd) {
        this.timeSelected = pd
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

.divleft {
  width: 50%;
  float: left;
  box-sizing: border-box;
  box-shadow: 3px 3px 3px 3px #8e9092;
}

.divright {
  width: 50%;
  float: right;
  box-sizing: border-box;      
  background: rgb(205, 219, 230);
  box-shadow: 3px 3px 3px 3px #8e9092;
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

hr {
  height: 1px;
  border: 0px;
  background:rgb(111, 111, 240);
}
</style>
