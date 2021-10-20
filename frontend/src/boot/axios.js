import axios from 'axios'

const baseURL = 'http://localhost:8000/'

const HTTPClient = axios.create({
  baseURL: baseURL
})
try {
  HTTPClient.defaults.xsrfCookieName = 'csrftoken'
  HTTPClient.defaults.xsrfHeaderName = 'X-CSRFToken'
} catch (e) {

}
// HTTPClient.defaults.withCredentials = true

export {
  HTTPClient
}
