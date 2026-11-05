// stone:job stone:math.circ_in
// stone:function circ_in_rs

#[no_mangle]
pub extern "C" fn circ_in_rs(t: f64) -> f64 {
    1.0 - (1.0 - t).sqrt()
}
