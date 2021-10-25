import { HTTPClient } from 'boot/axios'
import { handleError } from 'boot/exceptions'
// import { Notify } from 'quasar'

const travelsList = ({ commit }) => {
  return new Promise((resolve, reject) => {
    HTTPClient.get('core/travels/')
      .then(async (suc) => {
        await commit('SET_TRAVELS', suc.data)
        resolve(suc.data)
      })
      .catch(async (err) => {
        err = await err
        handleError(err)
        reject(err)
      })
  })
}

const longerTravels = ({ commit }) => {
  return new Promise((resolve, reject) => {
    HTTPClient.get('/core/travels/long_trips/')
      .then(async (suc) => {
        await commit('SET_LONGER_TRAVELS', suc.data)
        resolve(suc.data)
      })
      .catch(async (err) => {
        err = await err
        handleError(err)
        reject(err)
      })
  })
}

export {
  travelsList,
  longerTravels
}
