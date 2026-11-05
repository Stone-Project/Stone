// stone:job stone:math.quad_in_out
// stone:function quad_in_out_rs

#[no_mangle]
pub extern "C" fn quad_in_out_rs(t: f64) -> f64 {
    if t < 0.5 { 2.0 * t * t } else { -1.0 + (4.0 - 2.0 * t) * t }
}
