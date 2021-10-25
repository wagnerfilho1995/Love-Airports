<template>
  <q-layout view="lHh Lpr lFf" class="bg-grey-3">
    <q-header elevated class="bg-white text-grey-8">
      <q-toolbar style="height: 64px">
        <q-input class="GPL__toolbar-input" dense standout="bg-primary" v-model="search" placeholder="Buscar Aeroporto">
          <template v-slot:prepend>
            <q-icon v-if="search === ''" name="search" />
            <q-icon v-else name="clear" class="cursor-pointer" @click="search = ''" />
          </template>
        </q-input>
        <q-space />
        <div class="q-gutter-sm row items-center no-wrap">
          <q-btn round dense flat color="grey-8" icon="notifications">
            <q-badge color="red" text-color="white" floating>
              2
            </q-badge>
            <q-tooltip>Notifications</q-tooltip>
          </q-btn>
          <q-btn round flat>
            <q-avatar size="26px">
              <img src="https://cdn.quasar.dev/img/boy-avatar.png">
            </q-avatar>
            <q-tooltip>Account</q-tooltip>
          </q-btn>
        </div>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above :width="240">
      <q-scroll-area class="fit bg-primary">
        <div class="text-white" style="padding-top: 1rem; text-align: center">
          <span class="logo-title">
            Love
            <q-icon class="text-red" name="mdi-heart" />
            Airports
          </span>
          <q-list class="q-pa-none" dark bordless style="max-width: 280px; margin: 0px; padding-top: 1rem;">
            <q-item to="/travels">
              <q-item-section avatar>
                <q-icon color="white" name="mdi-earth" />
              </q-item-section>
              <q-item-section>
                <q-item-label class="text-white">Viagens</q-item-label>
              </q-item-section>
            </q-item>
            <q-item to="/data">
              <q-item-section avatar>
                <q-icon color="white" name="mdi-airplane" />
              </q-item-section>
              <q-item-section>
                <q-item-label class="text-white">Aeroportos</q-item-label>
              </q-item-section>
            </q-item>
            <!-- <q-item to="/">
              <q-item-section avatar>
                <q-icon color="white" name="mdi-airport" />
              </q-item-section>
              <q-item-section>
                <q-item-label class="text-white">Aeronaves</q-item-label>
              </q-item-section>
            </q-item> -->
          </q-list>
        </div>
      </q-scroll-area>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name: 'LoveAirportsLayout',
  data () {
    return {
      leftDrawerOpen: true,
      search: '',
      links1: [
        { icon: 'mdi-earth', text: 'Viagens', to: '/' },
        { icon: 'mdi-airplane', text: 'Aeroportos', to: '/data' },
        { icon: 'mdi-airport', text: 'Aeronaves', to: '/' },
        { icon: 'airplane_ticket', text: 'Passagens', to: '/' },
        { icon: 'mdi-seat-passenger', text: 'Passageiros', to: '/' }
      ]
    }
  },
  methods: {
    toggleLeftDrawer () {
      this.leftDrawerOpen.value = !this.leftDrawerOpen.value
    }
  }
}
</script>

<style scoped>
  .logo-title {
    text-align: center;
    font: normal normal bold 24px Roboto;
    letter-spacing: 0px;
    color: #FBFBFB;
    opacity: 1;
  }
</style>
