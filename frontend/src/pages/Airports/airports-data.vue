<template>
  <div class="q-pa-md">
    <q-toolbar>
      <q-btn flat round icon="arrow_back" @click="back()" />
      <q-toolbar-title>Aeroportos</q-toolbar-title>
    </q-toolbar>

    <q-card-section class="q-pt-2">
      <q-spinner
        v-if="loading"
        color="primary"
        size="3em"
      />
      <q-table
        v-else
        title="Encontre os aeroportos mais próximos e mais distantes do seu!"
        :data="data"
        :columns="columns"
        row-key="name"
        :pagination.sync="pagination"
        :filter="filter"
      >
        <template v-slot:top-right>
          <q-input
            outlined
            dense
            debounce="300"
            v-model="filter"
            style="width: 340px"
            placeholder="Procure pela sigla do seu aeroporto ..."
          >
            <template v-slot:append>
              <q-icon name="search" />
            </template>
          </q-input>
        </template>
      </q-table>
    </q-card-section>
  </div>
</template>

<script scoped lang="js" src="./airports-data.component.js"></script>
