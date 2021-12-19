(* Exercice 1 *)
(* 
type arbre = Nil | Noeud of arbre * arbre;;

let rec genere_complet = function
  | -1 -> Nil
  | n -> Noeud (genere_complet (n-1),genere_complet (n-1));;




let rec cheminement = function
  | Nil -> 0
  | Noeud (g,d) -> 1 + (cheminement g) + (cheminement d);; *)

(* cheminement vaut 2**(n+1) - 1 *)

(* Exercice 2 *)

(* type 'a arbre = Feuille of 'a | Noeud of 'a * 'a arbre * 'a arbre ;;

let ajout_numero arbre =
  let rec f arbre acc = match arbre with
    | Feuille a -> Feuille (acc,a)
    | Noeud (el,g,d) -> Noeud ((acc,el),f g (2*acc),f g (2*acc+1)) 
in f arbre 1;;
 *)




(* Exercice 3 *)

(* type arbre = Nil | Noeud of int * arbre * arbre ;;
let tree = Noeud (1,Noeud(2,Noeud (4,Noeud (7,Nil,Nil),Noeud (8,Nil,Nil)),Noeud (5,Nil,Nil)),Noeud (3,Noeud (6,Noeud (9,Nil,Nil),Noeud (10,Nil,Nil)),Nil))


let rec liste_etiquette arbre n = match arbre,n with 
  | Nil,_ ->[]
  | Noeud (el,g,d),0 -> [el]
  | Noeud (el,g,d),n -> (liste_etiquette g (n-1)) @ (liste_etiquette d (n-1))
 *)


(* Exercice 4 *)


(* type 'a arbre = Noeud of 'a * ('a arbre list) ;;
let tree = Noeud (1,[Noeud(2,[Noeud(6,[Noeud(7,[])])]);Noeud(3,[]);Noeud(4,[]);Noeud(5,[])])


let rec nb_feuille = function 
  | Noeud(el,[]) -> 1
  | Noeud(el,ab) -> let rec f = function
                        | [] -> 0
                        | h::q -> nb_feuille h + f q
                        in f ab;;


let rec hauteur = function
  | Noeud(el,[]) -> 0
  | Noeud(el,ab) -> 1 + let rec f = function
                        | [] -> 0
                        | h::q -> max (hauteur h) (f q)
                      in f ab;; *)



(* Exercice 5 *)

type arbre = Feuille | Noeud of arbre * arbre ;;


let rec strahler = function
  | Feuille -> 1
  | Noeud(g,d) -> let i = strahler g and j = strahler d in match i,j with
                                                    | i,j when i = j -> i + 1
                                                    | i,j -> max i j;;



(* Pour une hauteur h donnée, les arbres de complexité maximale sont les arbres complets dont le nombre de Stahler vaut h + 1. Les arbres de complexité minimale sont les arbres filiformes ou dégénérés (peigne) *)


(* Pour une hauteur h donnée, il y a 2**(h-1) arbres filiformes possibles. *)



(* 
let rec filiforme = function
  | 0 ->[]
  | 1 -> [Noeud (Feuille, Feuille)]
  | h -> let lst = filiforme (h-1) in
    let lst1 = List.map (function arb -> Noeud (Feuille, arb)) lst
    and lst2 = List.map (function arb -> Noeud (arb, Feuille)) lst in
    lst1 @ lst2 ;;
 *)



(* Exercice 6 *)

(* type arbre = Feuille | Noeud of arbre * arbre ;; *)


let fibo_arbre n = 
  let tab = Array.make (n+1) Feuille in
  for k = 2 to n do
    tab.(k) <- Noeud(tab.(k-1),tab.(k-2))
  done;
  tab.(n);;




(* Soit un arbre de Fibonacci A_k. Si k=0, A_k est de hauteur 0. Pour k>=1, A_k est de hauteur (k-1) (Par récurrence.) *)


(* Pour k\in N, P(n):"H(Ak_d) <=H(Ak_g) <= 1 + H(Ak_d)"

Initialisation : Ok

Hérédité. Soit k \in N. Supposons P(0),P(1),...,P(k).


H(Ak+1_g) = 1 + H(Ak_g)= 1+ H(Ak+1_d) (par définition)
Donc H(Ak+1_g)<=1+ H(Ak+1_d)

Et de même, H(Ak+1_d) <= H(Ak+1_g) *)


(* On construit la suite de fibonacci a_0 = a_1 = 1. a_n+2 = a_n+1 + a_n. On a alors nombre de feuilles de A_n = a_n et nombre de noeuds de A_n : N(A_n) = a_n - 1 (arbre binaire strict. ) *)


(* En utilisant les fonctions Strahler et fibo_arbre, on constate que le nombre de Strahler de A_n est $ \lfloor \frac{n}{2} \rfloor +1$. *)

(* Exercice 7 *)

(* Un arbre binaire à n+1 noeuds possède une racine, un arbre gauche possédant k noeuds et un arbre droit possédant n-k noeuds. Cela pour k \in [\![1,n]\!].

Donc il y c_k arbre de gauche possible et c_{n-k} arbre de droite possible. D'où c_{n+1} = \sum_{k=1}^n c_k c_{n-k} *)

(* On remplacer ici les noeuds possédant un seul fils par un même noeuds possédant ce même fils et un Nil en plus. Cela revient au cas de l'arbre binaire strict cela ne modifie pas notre relation. *)





(* Exercice 8 *)

(* On note Noeud (z, fils_g, fils_d). On distingue trois cas :
Si z est différent de x et de y, alors l'un appartient à fils_g, l'autre à fils_d. Mézalor l'ordre relatif au parcours est identique pour l'ordre préfixe et l'ordre suffixe.
CQNP.

Si y = z, y précède x dans l'ordre préfixe. CQNP 
Ainsi, x = z puis x précède y dans le parcours préfixe et le succède dans le parcours suffixe. *)




