<template>
    <div>
        <v-container>
            <v-row>
                <v-col cols="6">
                    <Formulario/>
                </v-col>
                <v-col cols="6">
                    <v-card class="pa-2">
                        <v-responsive class="overflow-auto" max-height="600">
                            <v-list>
                                <v-list-item v-for="(item, index) in listaVeiculos" :key="index">
                                    <v-list-item-icon>
                                        <v-icon left>mdi-car-side</v-icon>
                                    </v-list-item-icon>
                                    <v-list-item-content>
                                        <v-list-item-title v-text="item.veiculo"></v-list-item-title>
                                        <v-list-item-subtitle v-text="item.marca"></v-list-item-subtitle>
                                    </v-list-item-content>
                                    <v-list-item-action>
                                        <FormularioEdicao :dados="item"/>
                                    </v-list-item-action>
                                    <v-list-item-action>
                                        <v-btn icon @click="deletar(item.id)">
                                            <v-icon>mdi-trash-can-outline</v-icon>
                                        </v-btn>
                                    </v-list-item-action>
                                </v-list-item>
                            </v-list>
                        </v-responsive>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";
import Formulario from "@/components/Formulario";
import FormularioEdicao from "@/components/FormularioEdicao";


export default {
    name: "Home",
    components: {
        Formulario,
        FormularioEdicao
    },
    created() {
        this.retornarTodosVeiculos();
    },
    methods: {
        ...mapActions([
            "retornarTodosVeiculos",
            "deletarVeiculo",
        ]),

        deletar(ponto) {
            this.deletarVeiculo(ponto)
                .then(() => {
                    this.retornarTodosVeiculos()
                })
        },
    },
    computed: {
        ...mapGetters(["listaVeiculos"])
    }
}
</script>

<style scoped>

</style>