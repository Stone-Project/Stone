// stone:job stone:math.deg_norm
// stone:function deg_norm_rs

#[no_mangle]
pub extern "C" fn deg_norm_rs(d: f64) -> f64 {
    d.rem_euclid(360.0)
}
