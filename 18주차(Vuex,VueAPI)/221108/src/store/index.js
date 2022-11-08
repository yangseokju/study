import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [
      {
        title: '아메리카노',
        price: 3000,
        selected: false, // 초기값
        image:'https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[9200000000038]_20210430113202458.jpg'
      },
      {
      title: '녹차초코',
      price: 4500,
      selected: false, // 초기값
      image: 'https://image.istarbucks.co.kr/upload/store/skuimg/2022/03/[9200000002672]_20220311105511600.jpg'
      },
      {
      title: '블루베리요거트',
      price: 5000,
      selected: false, // 초기값
      image: 'https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[5210008063]_20210419104847612.jpg'
      },
    ],
    sizeList: [
      {
        name: 'small',
        price: 500,
        selected: false, //초기값
      },
      {
        name: 'medium',
        price: 1000,
        selected: false, //초기값
      },
      {
        name: 'large',
        price: 1500,
        selected: false, //초기값
      },
    ],
    totalprice:0,
    optionList: [
      {
        type: '샷',
        price: 500,
        count: 0,
      },
      {
        type: '펄',
        price: 1000,
        count: 0,
      },
      {
        type: '칼낮설',
        price: 1500,
        count: 0,
      },
     ],
  },
  getters: {
    totalOrderCount(state) {
      return state.orderList.length
    },
    totalOrderPrice(state) {
      if (state.orderList.length != 0) {
        let totaloption = state.orderList[state.orderList.length-1].options.reduce((total, x) => {
          return total + x.price * x.count
        }, 0)
        state.totalprice += (state.orderList[state.orderList.length-1].menu.price + state.orderList[state.orderList.length-1].size.price + totaloption)
      }
      return state.totalprice
    },
  },
  mutations: {
    addOrder: function (state) {
      const options = state.optionList
      state.menuList.forEach((menu) => {
        if (menu.selected) {
          state.sizeList.forEach((size) => {
            if (size.selected) {
              state.orderList.push({menu, size, options})
              size.selected=false
            }
          })
          menu.selected=false
        }
      })
      console.log(state.orderList)
    },
    updateMenuList: function (state, selectedMenu) {
      state.menuList.forEach((menu) => {
        if (menu.title === selectedMenu.title) {
          if (menu.selected) {
            menu.selected = false
          } else {
            menu.selected = true
          }
        } else {
          menu.selected = false
        }
      })
    },
    updateSizeList: function (state, selectedSize) {
      state.sizeList.forEach((size) => {
        if (size.name === selectedSize.name) {
          if (size.selected) {
            size.selected = false
          } else {
            size.selected = true
          }
        } else {
          size.selected = false
        }
      })
    },
    updateOptionList(state, newOption) {
      state.optionList.forEach((option) => {
        if (option.type === newOption.option.type) {
          if (newOption.flag === 1) {
            option.count += 1
          }
          else if (newOption.flag === 2) {
            if (option.count > 0) {
              option.count -= 1
            }
          }
        }
      })
    },
  },
  actions: {
    pickmenu(context, menu) {
      context.commit('updateMenuList', menu)
    },
    picksize(context, size) {
      context.commit('updateSizeList', size)
    },
    pickorder(context) {
      context.commit('addOrder')
    },
    increase(context, option) {
      context.commit('updateOptionList',option)
    },
    decrease(context, option) {
      context.commit('updateOptionList',option)
    },
  },
  modules: {
  }
})