// stone:job stone:math.circ_out
// stone:function circ_out_rs

#[no_mangle]
pub extern "C" fn circ_out_rs(t: f64) -> f64 {
    t.sqrt()
}
