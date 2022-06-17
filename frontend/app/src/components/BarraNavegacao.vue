<template>
    <div>
        <v-app-bar app color="grey lighten-4">
            <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
            <v-container>
                <v-toolbar class="elevation-0" color="grey lighten-4">
                    <v-toolbar-title>Tinnova Veículos</v-toolbar-title>
                </v-toolbar>
            </v-container>
        </v-app-bar>
        <v-navigation-drawer v-model="drawer" absolute temporary>
            <Menu/>
        </v-navigation-drawer>
    </div>
</template>

<script>
import Menu from "@/components/Menu";
export default {
    name: "BarraNevagacao",
    components: {
        Menu
    },
    data: () => ({
        drawer: false
    })
}
</script>

<style scoped>

</style>