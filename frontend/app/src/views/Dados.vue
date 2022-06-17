<template>
    <div>
        <v-container>
            <v-banner>Sobre a Base de Dados</v-banner>
            <v-row class="mt-3">
                <v-col>
                    <v-card>
                        <v-card-title>Veículos Não Vendidos</v-card-title>
                        <v-card-subtitle>{{ valorNaoVendidos }}</v-card-subtitle>
                    </v-card>
                </v-col>
                <v-col>
                    <v-card>
                        <v-card-title>Veículos Vendidos Na Ultima Semana</v-card-title>
                        <v-card-subtitle>{{ valorSemanal }}</v-card-subtitle>
                    </v-card>
                </v-col>
            </v-row>
            <v-row>
                <v-col>
                    <v-list>
                        <v-subheader>Quantidade Por Fabricantes</v-subheader>
                        <v-list-item v-for="(item, index) in listaFabricante" :key="index">
                            <v-list-item-content>
                                <v-list-item-title v-text="item.nome"></v-list-item-title>
                                <v-list-item-subtitle v-text="item.valor"></v-list-item-subtitle>
                            </v-list-item-content>
                        </v-list-item>
                    </v-list>
                </v-col>
                <v-col> <v-list>
                    <v-subheader>Quantidade Por Decadas</v-subheader>
                    <v-list-item v-for="(item, index) in listaDecada" :key="index">
                        <v-list-item-content>
                            <v-list-item-title v-text="item.ano"></v-list-item-title>
                            <v-list-item-subtitle v-text="item.valor"></v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                </v-list></v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
    name: "Dados",
    created() {
        this.retornarDados();
    },
    methods: {
        ...mapActions(["retornarDados"])
    },
    computed: {
        ...mapGetters([
            "valorNaoVendidos",
            "valorSemanal",
            "listaFabricante",
            "listaDecada"
        ])
    }
}
</script>

<style scoped>

</style>