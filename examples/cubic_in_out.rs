// stone:job stone:math.cubic_in_out
// stone:function cubic_in_out_rs

#[no_mangle]
pub extern "C" fn cubic_in_out_rs(t: f64) -> f64 {
    if t < 0.5 {
        4.0 * t * t * t
    } else {
        let u = 1.0 - t;
        1.0 - 4.0 * u * u * u
    }
}
