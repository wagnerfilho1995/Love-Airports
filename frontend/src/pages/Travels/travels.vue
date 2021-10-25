<template>
  <div class="q-pa-sm">
    <q-toolbar>
      <q-btn flat round icon="arrow_back" style="color: #333F48" @click="back()" />
      <q-toolbar-title><span class="title-page">Viagens</span></q-toolbar-title>
    </q-toolbar>

    <q-card-section class="q-pt-2">
      <q-spinner
        v-if="loading"
        color="primary"
        size="3em"
      />
      <q-table
        v-else
        title="Descubra quais são as viagens mais longas!"
        :data="data"
        :columns="columns"
        row-key="name"
        :pagination.sync="pagination"
      ></q-table>
    </q-card-section>
  </div>
</template>

<script scoped lang="js" src="./travels.component.js"></script>

<style scoped lang="scss" src="./travels.component.scss"></style>
