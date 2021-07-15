hljs.registerLanguage('algorithm', (hljs) => {
  return {
    name: 'algorithm',
    case_insensitive: true, 
    aliases: ['alg'],
    lexemes : '[\\\'àéèêâäöüÄÖÜßa-zA-Z]+',
    keywords: {
      keyword: 'algorithme retourner programme fonction procédure début ecrire écrire afficher lire si alors sinon fin tantque faire répéter jusqu\'à mod div pour de à pas non et ou ouex',
      literal: 'faux vrai nul'
    },
    contains: [
      {
        className: 'string',
        begin: '"', end: '"'
      },
      hljs.C_LINE_COMMENT_MODE,
      hljs.C_NUMBER_MODE
    ]
  };
});

