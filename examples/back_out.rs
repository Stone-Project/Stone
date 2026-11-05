// stone:job stone:math.back_out
// stone:function back_out_rs

#[no_mangle]
pub extern "C" fn back_out_rs(t: f64) -> f64 {
    let u = t - 1.0;
    1.0 + u * u * (2.70158 * u + 1.70158)
}
