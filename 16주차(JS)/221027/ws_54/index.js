/* 
  아래에 코드를 작성해주세요.
*/

const URL_API = 'http://ws.audioscrobbler.com/2.0/?method=track.search&track=Believe&api_key=1b0f9263281b4585aadc3a626e22bc04&format=json'
const inputTag = document.querySelector('.search-box__input')
const searchBtn = document.querySelector('.search-box__button')

let albums = new Array()
searchBtn.addEventListener('click',function fetchAlbums(page, limit) {
  let keyword = inputTag.value
  // inputTag.value = ""
  axios({
    method:'get',
    url:URL_API,
  })
  .then(response => {
    response.data.results.trackmatches.track.forEach(music => {
      if (music.name.includes(keyword)) {
        albums.push(music)
      }    
    });

    const divTag = document.querySelector('.search-result')
    albums.forEach((album) => {
      const divTag1 = document.createElement('div')
      divTag1.classList.add('search-result__card')
      divTag.appendChild(divTag1)

      const imgTag = document.createElement('img')
      imgTag.src = album.image[1]['#text']
      divTag1.appendChild(imgTag)

      const divTag2 = document.createElement('div')
      divTag2.classList.add('search-result__text')
      divTag1.appendChild(divTag2)

      const pTag = document.createElement('p')
      pTag.innerText = `${album.name}`
      const h2Tag = document.createElement('h2')
      h2Tag.innerText = `${album.artist}`
      divTag2.appendChild(h2Tag)
      divTag2.appendChild(pTag)
    })
  })
  .catch((error) => {
    alert('잠시 후 다시 시도해주세요')
  })
})

// 3번