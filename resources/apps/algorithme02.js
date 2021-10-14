
const nomCtrl = document.querySelector("#simulation-1 input[name='nom']");
const ageCtrl = document.querySelector("#simulation-1 input[name='age']");
const app = new Vue({
  el: "#simulation-1",
  data: {
    step: -1,
    nom: 'Raed',
    age: 16,
    message: ''
  },
  methods: {
    simuler: function (step) {
      this.step = step;
      if (step == 0) {
        Vue.nextTick(() => this.$refs.nom.focus());
      } else if (step == 1) {
        Vue.nextTick(() => this.$refs.age.focus());
      } else if (step == 2) {
        if (this.age > 18) {
          this.message = "Vous êtes majeur depuis " + (this.age - 18) + " ans";
        } else if (this.age < 18) {
          this.message = "Vous serez majeur dans " + (18 - this.age) + " ans";
        } else {
          this.message = "Vous êtes majeur à partir de cette année";
        }
      }
    }
  }
});

const app1 = new Vue({
  el: "#simulation-2",
  data: {
    step: -1,
    qte: 5,
    argent: 5000,
    message: ''
  },
  methods: {
    simuler: function (step) {
      this.step = step;
      if (step == 0) {
        Vue.nextTick(() => this.$refs.qte.focus());
      } else if (step == 1) {
        Vue.nextTick(() => this.$refs.argent.focus());
      } else if (step == 2) {
        const total = this.qte * 800;
        if (this.argent > total) {
          this.message = "Monnaie = " + (this.argent - total);
        } else if (this.argent < total) {
          this.message = "Manquant = " + (total - this.argent);
        } else {
          this.message = "A bientôt";
        }
      }
    }
  }
});

const app3 = new Vue({
  el: "#simulation-3",
  data: {
    step: -1,
    cmd1: 'Café',
    cmd2: 'Boisson gazeuse',
    cmd11: 'Café',
    cmd12: 'Boisson gazeuse',
    err: 'oui'
  },
  methods: {
    simuler: function (step) {
      this.step = step;
      if (step == 0) {
        Vue.nextTick(() => this.$refs.cmd1.focus());
      } else if (step == 1) {
        Vue.nextTick(() => this.$refs.cmd2.focus());
      } else if (step == 2) {
        Vue.nextTick(() => this.$refs.err.focus());
      } else if (step == 3) {
        this.err = this.err.trim().toLowerCase();
        this.cmd11 = this.cmd1;
        this.cmd12 = this.cmd2;
        if (this.err == 'oui') {
          this.cmd11 = this.cmd2;
          this.cmd12 = this.cmd1;
        }
      }
    }
  }
});

const app4 = new Vue({
  el: "#simulation-4",
  data: {
    step: -1,
    num: 5242442,
    message: ''
  },
  methods: {
    simuler: function (step) {
      this.step = step;
      if (step == 0) {
        Vue.nextTick(() => this.$refs.num.focus());
      } else if (step == 1) {
        this.num = +this.num;
        const u = this.num % 10;
        const d = Math.floor(this.num / 10) % 10;
        const c = Math.floor(this.num / 100) % 10;
        const m = Math.floor(this.num / 1000) % 10;
        if (u != 0 && d == (2 * u) && u == m && c == d) {
          this.message = "Vous êtes le gagnant du jour";
        } else {
          this.message = "Merci pour votre visite";
        }
      }
    }
  }
});

const app5 = new Vue({
  el: "#simulation-5",
  data: {
    step: -1,
    nom: 'Farida',
    moy: 8.95,
    disp_math: false,
    math: 9.0,
    disp_info: false,
    info: 9.0,
    message: ''
  },
  methods: {
    simuler: function (step) {
      this.step = step;
      if (step == 0) {
        Vue.nextTick(() => this.$refs.nom.focus());
      } else if (step == 1) {
        Vue.nextTick(() => this.$refs.moy.focus());
      } else if (step == 2) {
        this.moy = +this.moy;
        this.disp_math = false;
        this.disp_info = false;
        Vue.nextTick(() => {
          if (this.moy >= 10 || this.moy < 9) {
            this.simuler(4);
          } else {
            this.disp_math = true;
            this.disp_info = true;
            Vue.nextTick(() => this.$refs.math.focus());
          }
        });
      } else if (step == 3) {
        Vue.nextTick(() => this.$refs.info.focus());
      } else if (step == 4) {
        const arith = (+this.math + +this.info) / 2;
        this.moy = +this.moy;
        if (this.moy >= 10.0 || (this.moy >= 9.0 && arith >= 9.0)) {
          this.message = this.nom + " réussit";
        } else {
          this.message = this.nom + " redouble";
        }
      }
    }
  }
});