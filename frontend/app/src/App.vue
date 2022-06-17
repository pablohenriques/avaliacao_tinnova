<template>
  <v-app>
      <BarraNavegacao/>
      <v-main>
          <router-view/>
      </v-main>
  </v-app>
</template>

<script>
import BarraNavegacao from "@/components/BarraNavegacao";
export default {
    name: 'App',
    components: {
      BarraNavegacao
    },
    data: () => ({
        //
    })
};
</script>
