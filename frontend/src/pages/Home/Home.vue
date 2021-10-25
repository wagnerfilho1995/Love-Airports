<template>
  <div class="q-pa-md row items-start q-gutter-md">
    <q-toolbar>
      <q-toolbar-title
        ><span class="title-page"
          >Demografia dos Aeroportos</span
        ></q-toolbar-title
      >
    </q-toolbar>
    <q-card class="col-12 my-card">
      <q-card-section>
        <div class="row">
          <div class="col" style="align-self: center">
            <q-card-section class="q-pa-none">
              <span class="title-card vertical-bottom"
                >Distribuição nos estados do Brasil</span
              >
            </q-card-section>
          </div>
          <div class="col-auto">
            <div class="row">
              <q-icon size="lg" name="mdi-airport" color="primary" />
            </div>
          </div>
        </div>
      </q-card-section>
      <q-separator inset />
      <q-card-section>
        <canvas id="myChart"></canvas>
      </q-card-section>
    </q-card>
    <div>
      <div class="row">
        <div class="col" style="align-self: start">
          <q-card class="my-card bg-secondary text-white">
            <q-card-section>
              <div class="text-subtitle">Mais populoso</div>
              <div class="text-h6">{{ states[0] }}</div>
            </q-card-section>
            <q-card-section style="padding-top: 0px; padding-bottom: 0px">
              <span>O estado {{ states[0] }} possui um total de {{ airports[states[0]] }} aeroportos.</span>
            </q-card-section>
            <q-separator dark inset />
            <q-card-section style="padding-top: 0px;">
              <span>Outros também se destacam, como:</span>
              <div v-for="(state, index) in states.slice(1, 4)" :key="state.index">
                <span v-if="index == 2"> e {{  }} {{ state }}, com {{ airports[state] }} aeroportos.</span>
                <span v-else>{{ state }}, com {{ airports[state] }} aeroportos.</span>
              </div>
            </q-card-section>
          </q-card>
        </div>
      </div>
    </div>
  </div>
</template>

<script scoped lang="js" src="./home.component.js"></script>
<style scoped lang="scss" src="./home.component.scss"></style>
