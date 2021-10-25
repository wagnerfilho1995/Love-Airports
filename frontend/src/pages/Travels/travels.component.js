import { mapActions, mapState } from 'vuex'

export default {
  data () {
    return {
      page: 1,
      columns: [],
      data: [],
      loading: true,
      pagination: {
        rowsPerPage: 30
      }
    }
  },
  computed: {
    ...mapState('Travels', ['travels'])
  },
  methods: {
    ...mapActions('Travels', [
      'longerTravels'
    ]),
    back () {
      this.$router.back()
    },
    always2 (n) {
      return n > 9 ? '' + n : '0' + n
    },
    getFormattedDuration (date1, date2) {
      const diffTime = Math.abs(date2 - date1)
      let minutes = diffTime / 1000 / 60
      const hours = Math.floor(minutes / 60)
      minutes = minutes - (hours * 60)
      return this.always2(hours) + ':' + this.always2(minutes)
    },
    getFormattedDate (date) {
      return (date.getDate() +
        '/' + (date.getMonth() + 1) +
        '/' + date.getFullYear())
    },
    async setData (dados) {
      for (const [key, travel] of Object.entries(dados)) {
        console.log(key, travel)
        this.data.push(
          {
            departure_date: this.getFormattedDate(new Date(travel.departure_date)),
            origin: travel.origin.iata + ' - ' + travel.origin.city + ', ' + travel.origin.state,
            destination: travel.destination.iata + ' - ' + travel.destination.city + ', ' + travel.destination.state,
            aircraft: travel.itinerary.aircraft.manufacturer + ' - ' + travel.itinerary.aircraft.model,
            duration_h: this.getFormattedDuration(new Date(travel.itinerary.departure_time), new Date(travel.itinerary.arrival_time)),
            dist: travel.dist.toFixed(2)
          }
        )
      }
    },
    setColumns () {
      this.columns.push({ name: 'departure_date', align: 'center', label: 'Data', field: 'departure_date', sortable: true })
      this.columns.push({ name: 'origin', align: 'center', label: 'Origem', field: 'origin', sortable: true })
      this.columns.push({ name: 'destination', align: 'center', label: 'Destino', field: 'destination', sortable: true })
      this.columns.push({ name: 'aircraft', align: 'center', label: 'Aeronave', field: 'aircraft', sortable: true })
      this.columns.push({ name: 'duration_h', align: 'center', label: 'Duração', field: 'duration_h', sortable: true })
      this.columns.push({ name: 'dist', align: 'center', label: 'Distância (km)', field: 'dist', sortable: true })
    },
    async getTravels () {
      await this.longerTravels()
      this.setColumns()
      await this.setData(this.travels)
      this.loading = false
    }
  },
  created () {
    this.getTravels()
  }
}
