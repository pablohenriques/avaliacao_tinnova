<template>
    <div>
        <v-container>
            <v-list rounded>
                <v-subheader>OPÇÕES</v-subheader>
                <v-list-item-group>
                    <v-list-item v-for="(item, index) in opcoes" :key="index" :to="item.path">
                        <v-list-item-icon>
                            <v-icon v-text="item.icone"></v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                            <v-list-item-title v-text="item.texto"></v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </v-list-item-group>
            </v-list>
        </v-container>
    </div>
</template>

<script>
export default {
    name: "Menu",
    data:() => ({
        opcoes: [
            {texto: 'Home', icone: 'mdi-home', path: '/'},
            {texto: 'Dados', icone: 'mdi-chart-bar', path: 'dados'},
        ]
    })
}
</script>
