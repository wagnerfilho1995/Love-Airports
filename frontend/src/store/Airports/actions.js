import { HTTPClient } from 'boot/axios'
import { handleError } from 'boot/exceptions'
// import { Notify } from 'quasar'

const airportsList = ({ commit }) => {
  return new Promise((resolve, reject) => {
    HTTPClient.get('core/airports/')
      .then(async (suc) => {
        await commit('SET_AIRPORTS', suc.data)
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
  airportsList
}
