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

const airportsDemography = ({ commit }) => {
  return new Promise((resolve, reject) => {
    HTTPClient.get('core/airports/get_airports_demography/')
      .then(async (suc) => {
        await commit('SET_AIRPORTS_DEMOGRAPHY', suc.data)
        resolve(suc.data)
      })
      .catch(async (err) => {
        err = await err
        handleError(err)
        reject(err)
      })
  })
}

const airportsDistances = ({ commit }) => {
  return new Promise((resolve, reject) => {
    HTTPClient.get('core/airports/get_airports_distance/')
      .then(async (suc) => {
        await commit('SET_AIRPORTS_DISTANCES', suc.data)
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
  airportsList,
  airportsDemography,
  airportsDistances
}
