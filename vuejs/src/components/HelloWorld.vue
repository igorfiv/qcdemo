<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">
      <v-sheet width="50%" class="mx-auto mb-10">
        <form @submit.prevent="submitForm">
        <v-text-field
          v-model="state.value_a"
          :error-messages="v$.value_a.$errors.map(e => e.$message)"
          label="value_a"
          required
          @input="v$.value_a.$touch"
          @blur="v$.value_a.$touch"
        ></v-text-field>
        <v-text-field
          v-model="state.value_b"
          :error-messages="v$.value_b.$errors.map(e => e.$message)"
          label="value_b"
          required
          @input="v$.value_b.$touch"
          @blur="v$.value_b.$touch"
        ></v-text-field>
        <v-text-field
          v-model="state.target"
          :error-messages="v$.target.$errors.map(e => e.$message)"
          label="target"
          required
          @input="v$.target.$touch"
          @blur="v$.target.$touch"
        ></v-text-field>
        <v-radio-group v-model="state.radios">
          <v-radio label="fsolve method" value="fsolve"></v-radio>
          <v-radio label="Newton method" value="newton"></v-radio>
        </v-radio-group>
        <v-btn
          class="me-4"
          type="submit"
        >
          submit
        </v-btn>
      </form>
      </v-sheet>

      <v-divider v-if="result && result > 0" ></v-divider>

      <v-sheet v-if="result && result > 0" width="50%" class="mx-auto">
        Result: {{ result }}
      </v-sheet>
    </v-responsive>
  </v-container>
</template>

<script setup>
  import { reactive, ref } from 'vue'
  import { useVuelidate } from '@vuelidate/core'
  import { required, numeric, minValue } from '@vuelidate/validators'
  import axios from 'axios'

  const initialState = {
    value_a: '',
    value_b: '',
    target: '',
    radios: 'fsolve',
  }

  const state = reactive({
    ...initialState,
  })

  const rules = {
    value_a: {required, numeric, minValue: minValue(1)},
    value_b: {required, numeric, minValue: minValue(1)},
    target: {required, numeric, minValue: minValue(1)},
  }

  const v$ = useVuelidate(rules, state)
  const result = ref(0)

  const calculateResult = () => {
    axios
      .get(`http://localhost:8008/calculate/?value_a=${state.value_a}&value_b=${state.value_b}&target=${state.target}&method=${state.radios}`)
      .then((response) => {
        result.value = response.data.result; // 👈 get just results
      });
  };
  const submitForm = () => {
    const result = v$.value.$validate();
    result.then((res) => {
      if (res) {
        calculateResult()
      }
    }).catch((err) => {
      console.log(err);
    })
  }

</script>
