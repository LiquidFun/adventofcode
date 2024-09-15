let rec process nums i =
  match nums.(i) with
  | 1 -> nums.(nums.(i+3)) <- nums.(nums.(i+1)) + nums.(nums.(i+2)); process nums (i+4)
  | 2 -> nums.(nums.(i+3)) <- nums.(nums.(i+1)) * nums.(nums.(i+2)); process nums (i+4)
  | _ -> nums.(0)
  
let with_a_b nums n = 
  let memory = Array.copy nums in
  memory.(1) <- n / 100;
  memory.(2) <- n mod 100;
  process memory 0

let find_part2 nums =
  List.init 10000 Fun.id |> List.find (fun x -> (with_a_b nums x) == 19690720)

let () = 
  let nums = input_line stdin |> String.split_on_char ',' |> List.map int_of_string |> Array.of_list in
  with_a_b nums 1202 |> Printf.printf "%d\n";
  find_part2 nums |> print_int