// stone:job stone:math.circ_in_out
// stone:function circ_in_out_rs

#[no_mangle]
pub extern "C" fn circ_in_out_rs(t: f64) -> f64 {
    if t < 0.5 {
        0.5 * (1.0 - (1.0 - 2.0 * t).sqrt())
    } else {
        0.5 * ((2.0 * t - 1.0).sqrt() + 1.0)
    }
}
