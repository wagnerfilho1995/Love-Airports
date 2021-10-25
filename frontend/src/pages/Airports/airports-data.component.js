import { mapActions, mapState } from 'vuex'

export default {
  data () {
    return {
      page: 1,
      columns: [],
      data: [],
      filter: '',
      loading: true,
      pagination: {
        rowsPerPage: 20
      }
    }
  },
  computed: {
    ...mapState('Airports', ['airports'])
  },
  methods: {
    ...mapActions('Airports', [
      'airportsDistances'
    ]),
    back () {
      this.$router.back()
    },
    async setData (dados) {
      for (const [key, airport] of Object.entries(dados)) {
        console.log(key, airport)
        this.data.push(
          {
            iata: airport.iata,
            city: airport.city,
            state: airport.state,
            closer_iata: airport.closer.iata + ' - ' + airport.closer.city + ', ' + airport.closer.state,
            closer_dist: airport.closer.dist.toFixed(2),
            faraway_iata: airport.faraway.iata + ' - ' + airport.faraway.city + ', ' + airport.faraway.state,
            faraway_dist: airport.faraway.dist.toFixed(2)
          }
        )
      }
    },
    setColumns () {
      this.columns.push({ name: 'iata', align: 'center', label: 'Aeroporto', field: 'iata', sortable: true })
      this.columns.push({ name: 'city', align: 'center', label: 'Cidade', field: 'city', sortable: true })
      this.columns.push({ name: 'state', align: 'center', label: 'Estado', field: 'state', sortable: true })
      this.columns.push({ name: 'closer_iata', align: 'center', label: 'Aeroporto mais próximo', field: 'closer_iata', sortable: true })
      this.columns.push({ name: 'closer_dist', align: 'center', label: 'Distância (Km)', field: 'closer_dist', sortable: true })
      this.columns.push({ name: 'faraway_iata', align: 'center', label: 'Aeroporto mais longe', field: 'faraway_iata', sortable: true })
      this.columns.push({ name: 'faraway_dist', align: 'center', label: 'Distância (Km)', field: 'faraway_dist', sortable: true })
    },
    async getAirports () {
      await this.airportsDistances()
      this.setColumns()
      await this.setData(this.airports)
      this.loading = false
    }
  },
  created () {
    this.getAirports()
  }
}
