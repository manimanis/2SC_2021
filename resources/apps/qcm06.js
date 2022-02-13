document.addEventListener("DOMContentLoaded", () => {
  hljs.initHighlighting();
  const enonce_qcm = document.querySelector("#enonce-qcm");
  const q_elems = enonce_qcm.querySelectorAll("#enonce-qcm .question");
  const questions = [];
  q_elems.forEach(question => {
    const qobj = {};
    qobj.enonce = question.querySelector(".enonce").innerHTML;
    qobj.propositions = [];
    qobj.is_single = question.querySelector(".propositions").dataset["issingle"].toLowerCase() == "true";
    question.querySelectorAll(".propositions .proposition").forEach(
      proposition => {
        qobj.propositions.push(proposition.innerHTML);
      }
    );
    questions.push(qobj);
  });
  const app = new Vue({
    el: "#qcm",
    data: {
      num_question: 0,
      nbr_questions: questions.length,
      questions: questions,
      id: enonce_qcm.dataset['id'],
      titre: enonce_qcm.dataset['titre'],
      classe: enonce_qcm.dataset['classe'],
      description: enonce_qcm.dataset['description'],
      _nbr_questions_vides: questions.length,
      rep_array: questions
        .map((question, idx) => {
          if (question.is_single) {
            return ""; // `${idx+1}${String.fromCharCode(65+Math.floor(Math.random() * 4))}`; 
          }
          return []; // [`${idx+1}${String.fromCharCode(65+Math.floor(Math.random() * 4))}`];
        }),
      nom_prenom: "", // "Mohamed Anis MANI",
      errors: [],
      error_message: "",
      is_sent: false
    },
    computed: {
      nbr_questions_vides: function () {
        this._nbr_questions_vides = 0;
        for (let rep of this.rep_array) {
          if (rep.length == 0) {
            this._nbr_questions_vides++;
          }
        }
        return this._nbr_questions_vides;
      }
    },
    methods: {
      nextQuestion: function () {
        if (this.num_question < this.nbr_questions - 1) {
          this.gotoQuestion(this.num_question + 1);
        }
      },
      prevQuestion: function () {
        if (this.num_question > 0) {
          this.gotoQuestion(this.num_question - 1);
        }
      },
      gotoQuestion: function (num_question) {
        this.num_question = num_question;
      },
      resetForm: function () {
        this.rep_array = questions
          .map((question, idx) => {
            if (question.is_single) {
              return "";
            }
            return [];
          });
        this.nom_prenom = "";
      },
      submitAnswers: function () {
        if (this.nbr_questions_vides > 0) {
          alert("Soumission impossible vous devez répondre à toutes les questions !");
          return;
        }
        this.nom_prenom = this.nom_prenom.trim();
        if (this.nom_prenom == "") {
          alert("Soumission impossible vous devez indiquer votre nom & prénom !");
          return;
        }

        const data = new FormData();
        data.append("qcm_id", this.id);
        data.append("nom_prenom", this.nom_prenom);
        data.append("questions_count", this.rep_array.length);
        this.rep_array.forEach((rep, idx) => {
          if (Array.isArray(rep)) {
            data.append(`q${idx + 1}`, rep.join(""));
          } else {
            data.append(`q${idx + 1}`, rep);
          }
        });
        this.errors = [];
        fetch("saveanswer.php", {
          method: 'post',
          body: data,
        })
          .then(response => response.json())
          .then(data => {
            this.is_sent = true;
            if (data['isok']) {
              this.error_message = "Votre réponse a été envoyée.";
              this.resetForm();
            } else {
              this.error_message = "Votre réponse n'a pas été envoyée.";
              this.errors = data['errors'];
            }
          })
          .catch(err => {
            this.is_sent = true;
            this.errors = [err];
            this.error_message = "Erreur : votre réponse n'a pas été envoyée.";
          });
      }
    }
  });
});